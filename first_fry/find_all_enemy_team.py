import pyautogui
import time
import os

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
                os.system("python report_enemy.py")
                
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