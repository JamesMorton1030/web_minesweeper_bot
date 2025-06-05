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
    move_mouse_around_box()

def move_mouse_around_box():
    # Define the box coordinates (x1, y1, x2, y2)
    box = (100, 100, 200, 200)  # Example coordinates

    # Move the mouse around the box
    start_time = time.time()
    duration = 6  # Ensure the movement respects the duration limit
    for x in range(box[0], box[2] + 1):
        for y in range(box[1], box[3] + 1):
            if time.time() - start_time >= duration:
                return  # Exit the function if duration is exceeded
            pyautogui.moveTo(x, y)
            time.sleep(0.01)  # Small delay to visualize movement

