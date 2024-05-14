import pyautogui
import time

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
find_and_click_image('your_image_3.png')
time.sleep(1)
find_and_click_image('your_image.png')
time.sleep(1)
find_and_click_image('your_image_2.png')
time.sleep(1)
find_and_click_image('your_image_5.png')
time.sleep(1)
find_and_click_image('your_image_4.png')