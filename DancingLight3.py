# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:43:07 2024

@author: Morteza
"""

import cv2
import numpy as np
import random

# Get screen size (for filling the laptop screen)
screen_width = 1920
screen_height = 1080

# Initialize a blank image
frame = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

# Parameters for wave effect
center_x, center_y = screen_width // 2, screen_height // 2
max_radius = int(np.sqrt(center_x**2 + center_y**2)) + 100  # Radius to cover the whole screen
num_waves = 20  # Number of waves

# Create a window that fills the screen
cv2.namedWindow('Dancing Light Waves', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Dancing Light Waves', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Function to generate random color
def random_color():
    return [random.randint(0, 255) for _ in range(3)]

# Create video
while True:
    frame[:] = 0  # Clear the frame

    # Generate expanding circles (waves) with random colors
    for i in range(num_waves):
        radius = int(max_radius * i / num_waves)
        color = random_color()
        cv2.circle(frame, (center_x, center_y), radius, color, thickness=2)

    # Display the frame
    cv2.imshow('Dancing Light Waves', frame)
    
    # Break loop if 'q' is pressed
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# Release the window
cv2.destroyAllWindows()
