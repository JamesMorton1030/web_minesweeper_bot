import webbrowser
import subprocess
import os
import pyautogui
import time

def open_minesweeper_website():
    """Opens the default browser to www.minesweeper.com."""
    url = "https://minesweeperonline.com/#beginner"
    webbrowser.open(url)

def start_mine_script():
    find_start()
    move_mouse_around_box(2)
    

def move_mouse_around_box(duration):
    # Define the box coordinates (x1, y1, x2, y2)
    start_x, start_y = pyautogui.position()  # Get current mouse position

    for _ in range(5):
        pyautogui.moveTo(start_x + 24, start_y)
        start_x += 24  # Update the starting x-coordinate for the next move
        time.sleep(0.5)  # Small delay between movements

def find_start():
    
    try:
        # Locate the cell with id "cell_8_8"
        print("Searching for the Minesweeper cell...")
        cell = pyautogui.locateOnScreen('images/beginnerSweeperBoard.png')
        if cell:
            print  (f"Cell found")
            pyautogui.moveTo(cell.left + cell.width / 2, cell.top + cell.height / 2)
            print("Cell found and mouse moved to its center.")
        else:
            print("Cell not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {e}")