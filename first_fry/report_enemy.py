import pyautogui
import time
import os
import pyperclip

def find_and_click_image(image_path):
    try:
        # Locate the image on the screen with a confidence level
        location = pyautogui.locateOnScreen(image_path, confidence=0.9)  # Adjust the confidence as necessary

        if location:
            # Get the center of the found image
            center = pyautogui.center(location)
            # Move the cursor to the center of the image and click
            pyautogui.moveTo(center)
            pyautogui.click()
        else:
            print("Image not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_image.png' with the path to your screenshot
find_and_click_image('your_image_8.png')
time.sleep(1)
find_and_click_image('your_image_9.png')
time.sleep(1)
find_and_click_image('your_image_10.png')
time.sleep(1)
find_and_click_image('your_image_11.png')
time.sleep(1)
find_and_click_image('your_image_12.png')
time.sleep(1)
find_and_click_image('your_image_14.png')

pyperclip.copy("CHEATING")
pyautogui.hotkey('ctrl', 'v') 

time.sleep(1)
find_and_click_image('your_image_15.png')
time.sleep(1)
find_and_click_image('your_image_17.png')
time.sleep(1)
find_and_click_image('your_image_16.png')
