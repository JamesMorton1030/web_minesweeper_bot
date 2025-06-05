import webbrowser
import subprocess
import os
import pyautogui
import time

def open_minesweeper_website():
    """Opens the default browser to www.minesweeper.com."""
    url = "https://www.minesweeper.online/new-game"
    webbrowser.open(url)

def start_mine_script():
    duration = 6  # Example: run for 60 seconds
    start_time = time.time()
    while time.time() - start_time < duration:
        move_mouse_around_box()

def move_mouse_around_box():
    # Define the box coordinates (x1, y1, x2, y2)
    box = (100, 100, 200, 200)  # Example coordinates

    # Move the mouse around the box
    for x in range(box[0], box[2] + 1):
        for y in range(box[1], box[3] + 1):
            pyautogui.moveTo(x, y)
            time.sleep(0.01)  # Small delay to visualize movement

