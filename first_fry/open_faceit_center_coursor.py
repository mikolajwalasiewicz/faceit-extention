import webbrowser
import pyautogui
import time
import os

def open_browser_and_center(url):
    # Open the web browser with the specified URL
    webbrowser.open(url)
    
    # Wait for the browser to open
    time.sleep(5)  # Adjust the delay as needed for your browser to open

    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    
    # Calculate the center position
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    # Move the mouse cursor to the center of the screen
    pyautogui.moveTo(center_x, center_y, duration=0.5)

if __name__ == "__main__":
    url = "https://www.faceit.com"
    print(f"Opening {url} and centering the mouse cursor in 5 seconds...")
    open_browser_and_center(url)
    print("Mouse cursor moved to the center of the screen.")
    os.system("python find_latest_match.py")
