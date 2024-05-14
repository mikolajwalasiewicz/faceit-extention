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

def find_and_click(image_path, max_clicks=10):
    click_count = 0  # Initialize click counter

    # Loop until the maximum number of clicks is reached
    while click_count < max_clicks:
        try:
            # Find all matches on the screen
            positions = list(pyautogui.locateAllOnScreen(image_path, confidence=0.8))
            if not positions:
                print("No more crosses found, exiting.")
                break

            for pos in positions:
                # Get the center of the found image
                center = pyautogui.center(pos)
                # Move the cursor to the center of the image
                pyautogui.moveTo(center)
                # Click the center
                pyautogui.click()
                click_count += 1  # Increment the click counter
                print(f"Clicked at {center}, total clicks: {click_count}")
                #os.system("python report_enemy.py")
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

                # Check if maximum clicks reached
                if click_count >= max_clicks:
                    print("Reached maximum number of clicks.")
                    return

                # Pause between clicks
                time.sleep(0.5)

        except pyautogui.ImageNotFoundException:
            print("Image not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Replace with the path to your red cross image
find_and_click('your_image7.png')