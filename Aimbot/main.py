import torch
import mss
import numpy as np
import cv2
import keyboard
import time
import pyautogui

weight = 'PATH OF THE WEIGHT FILE'
# Load the YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "custom", path=weight)

# Initialize screen capture
with mss.mss() as sct:
    # Print available monitors
    print(sct.monitors)
    
    # Define monitor to capture (adjust according to your setup)
    monitor = sct.monitors[1]  # Assuming the first monitor

    # Main loop
    while True:
        t = time.time()
        
        try:
            # Capture screen
            image = np.array(sct.grab(monitor))
        except mss.exception.ScreenShotError as e:
            print(f"Screen capture failed: {e}")
            break
        
        # Perform object detection
        results = model(image)
        
        #When the ai detects an objext, it will store its position in a tensor along with its class number.
        results_list = results.xyxy[0].tolist() #converting tensor with positional data into a list
        
        if len(results_list) > 0:
            
            # Confidance data is stored at the [0][4] position of the list. 
            # If confidance is above 0.35 the program will continue. This filters out false detections.
            if results_list[0][4] > 0.35:
                # Class number is stored at the [0][5] position of the list.
                # Indices 15 and 16 correspond to the 'zombie' and 'wither skeleton' classes respectively in the dataset.yaml file.
                if results_list[0][5] == 15 or results_list[0][5] == 16:
                    
                    x = int(results_list[0][2])
                    y = int(results_list[0][3])
                    
                    # width = max width - min width
                    width = int(results_list[0][2] - results_list[0][0])
                    # height = max height - min height
                    height = int(results_list[0][3] - results_list[0][1])
                    # Centering the AI's aim.
                    # Multiplying the pposition by a certain factor to deal with any offsets cause by the games. 
                    # This factor need to be tweaked depending on the game.
                    x_position = (0.37 * ((x - (width/2)) - pyautogui.position()[0]))
                    y_position = (0.30 * ((y - (height/2)) - pyautogui.position()[1]))
                    # Ensuring that the AI does not spiral out of control when trageting objects
                    pyautogui.moveRel(x_position,y_position) # AI moves croshair to to the object's position
                    pyautogui.click() # AI shoots
                    pyautogui.moveRel(-x_position,-y_position) #AI moves croshair back to original position.
        
        
        
        
        
        # Display results
        cv2.imshow('Screen Capture', np.squeeze(results.render()))
        
        # Print FPS
        print('FPS: {:.2f}'.format(1 / (time.time() - t))) 
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()
