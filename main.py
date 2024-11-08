import pyautogui, sys
import time
import pydirectinput
import keyboard
import pygetwindow as gw
import win32gui
import win32con

import SelectWindow

def main():
    # Initialize Pyautogui
    pyautogui.FAILSAFE = True

    try:
        # Check if the user presses 'q' to stop the program
        if keyboard.is_pressed('q'):
            print("\nProgram stopped by user")

        # Initialize the SelectWindow instance for the window titled "Brown"
        sWin = SelectWindow.SelectWindow("Brown")
        time.sleep(2)

        # Print the matching window details
        print(sWin.matching_window)

        # Capture the screenshot of the window
        screenshot = pyautogui.screenshot("test.png",region=(
        sWin.matching_window.left, sWin.matching_window.top, sWin.matching_window.width, sWin.matching_window.height))

        # Locate the 'spacetest.png' image in the screenshot
        spacebutton = pyautogui.locateOnScreen('home.png', screenshot, confidence=0.85)
        print(f"Location {spacebutton}")

        # If found, click on the button
        if spacebutton:
            pyautogui.click(spacebutton)

    except KeyboardInterrupt:
        print("Stopped")

def doDailies():






#Focus Window and Center
def getWindow(title):

    #title = "test"

    # Get MatchingTitle
    matching_window = next((win for win in gw.getAllWindows() if title in win.title), None)

    if matching_window:
        # Activate the window
        matching_window.activate()

        # Get screen and window dimensions
        screen_width, screen_height = pyautogui.size()
        window_width, window_height = matching_window.width, matching_window.height

        # Calculate the position to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Move the window to the center of the screen
        matching_window.moveTo(x, y)



    else:
        print(f"No window found with title containing '{title}'")

def testing():
    keep_going = True
    if (keep_going):
        if (keyboard.is_pressed('enter')):
            print("Starting Script")
            keep_going = False
        else:
            print("start")

def isRunning():
    run = True
    keep_going = True

    while(run):
        if (keyboard.is_pressed('ctrl') and keyboard.is_pressed("z")):
            run = False
        if(keep_going):
            if (keyboard.is_pressed('enter')):
                print("Starting Script")
                keep_going = False
        else:
            # run scriptsw

            pydirectinput.keyDown('w')
            time.sleep(1)
            pydirectinput.keyUp('w')
            keep_going = True

            print("Script Done")


if __name__ == "__main__":
    main()
