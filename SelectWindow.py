import keyboard
import pyautogui
import pygetwindow as gw
import time

# Class for window
class SelectWindow:

    def __init__(self, title):
        self.title = title
        self.matching_window = None
        self.win_width, self.win_height = pyautogui.size()  # Screen size
        self.app_width = None
        self.app_height = None
        self.match_window()

    def match_window(self):
        # Find the first window matching the title
        self.matching_window = next((win for win in gw.getAllWindows() if self.title in win.title), None)

        print(self.matching_window)

        if self.matching_window:
            # Activate the window
            self.matching_window.activate()

            # Get the window's dimensions
            self.app_width, self.app_height = self.matching_window.width, self.matching_window.height

            # Calculate the position to center the window
            x = (self.win_width - self.app_width) // 2
            y = (self.win_height - self.app_height) // 2

            # Move the window to the center of the screen
            self.matching_window.moveTo(x, y)

            print(f"Window '{self.title}' centered at ({x}, {y})")
        else:
            print(f"No window found with the title: {self.title}")
    def getAppSize(self):
        return self.app_width, self.app_height

    def getWinSize(self):
        return self.win_width, self.win_height

    def appBorder(self):
        # Assign window boundaries
        left, top, right, bottom = self.matching_window.left, self.matching_window.top, self.matching_window.right, self.matching_window.bottom


        print(left,top,right,bottom)

        centerY = (top + bottom) // 2
        centerX = (right + left) // 2

        # Define corner positions
        self.corners = [
            (left - 1, top),  # Top-left 0
            (centerX, top),  # Top-center 1
            (right - 1, top),  # Top-right 2
            (right - 1, centerY),  # Right-center 3
            (right - 1, bottom - 1),  # Bottom-right 4
            (centerX, bottom - 1),  # Bottom-center 5
            (left, bottom - 1),  # Bottom-left 6
            (left + 9, centerY)  # Left-center 7
        ] # 0 - 7

        # Move the mouse to (left, centerTest) and then to (right, centerTest)

        pyautogui.moveTo(self.corners[7], duration=2)  # Move to the left-center first
        time.sleep(1)  # Wait for 1 second
        pyautogui.dragTo(self.corners[3], duration=2)  # Drag to the right-center over 2 seconds


        # Move the mouse to each corner with a short pause in between
        for corner in self.corners:
            # Check if the user pressed 'q' to stop the program
            try:
                #pyautogui.moveTo(corner[0], corner[1], duration=0.2)  # Moves with a 0.5-second duration for visibility
                time.sleep(0.2)  # Pause for a second at each corner
            except KeyboardInterrupt:
                print("Stop")

