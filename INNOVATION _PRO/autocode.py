import pyautogui
import time
import sys

# Safety feature - failsafe
pyautogui.FAILSAFE = True

def main():
    try:
        # Wait for WhatsApp to be loaded
        print("Waiting for WhatsApp to load (10 seconds)...")
        time.sleep(10)
        
        # Phone number and message to send
        phone_number = "+919113803759"
        message = "from Python! This is an automated message."
        
        # Get screen size for coordinate validation
        screen_width, screen_height = pyautogui.size()
        print(f"Screen size: {screen_width}x{screen_height}")
        
        # Click on the search bar - using coordinates
        print("Clicking search bar...")
        search_x = screen_width // 4  # Adjust this value as needed
        search_y = 100                # Adjust this value as needed
        pyautogui.click(x=search_x, y=search_y)
        print(f"Clicked at coordinates: {search_x}, {search_y}")
            
        time.sleep(2)
        
        # Type the phone number in the search bar
        print(f"Typing the phone number: {phone_number}")
        pyautogui.write(phone_number, interval=0.1)
        time.sleep(3)
        
        # Press 'Enter' to open the chat
        print("Opening the chat...")
        pyautogui.press('enter')
        time.sleep(5)
        
        # Type the message
        print(f"Typing the message: {message}")
        pyautogui.write(message, interval=0.05)
        time.sleep(1)
        
        # Press 'Enter' to send the message
        print("Sending the message...")
        pyautogui.press('enter')
        time.sleep(1)
        
        print(f"Message sent to {phone_number}!")
        
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(0)
    except pyautogui.FailSafeException:
        print("\nMouse moved to corner - emergency stop activated.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("WhatsApp Automation Script (Coordinate Version)")
    print("Note: Make sure WhatsApp Web is open and visible on your screen.")
    print("Press Ctrl+C to stop the script at any time.")
    main()