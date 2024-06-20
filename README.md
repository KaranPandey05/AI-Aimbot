# AI-Aimbot
 This Python script implements a basic aimbot using MSS, OpenCV, PyTorch, and YOLOv5. The software captures the screen, detects specific entities (zombies and wither skeletons) in Minecraft, and auto-locks and attacks them. The aimbot identifies these entities based on pre-trained weights for the YOLOv5 model, ensuring accurate detection.

Key functionalities include:

Screen Capture: Continuously captures the screen using MSS.
Object Detection: Uses the YOLOv5 model to detect entities within the captured screen.
Targeting and Attacking: If a zombie or wither skeleton is detected with confidence above 0.35, the script calculates their positions and moves the mouse to target and attack them.

This software is designed for educational purposes to demonstrate basic botting techniques in Python.
