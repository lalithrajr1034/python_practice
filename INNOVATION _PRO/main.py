
import pyautogui
import time
import re
import platform
import pandas as pd
from dataclasses import dataclass
from typing import List


# ==============================================
#                  DATA MODELS                  
# ==============================================
@dataclass
class Contact:
    """Represents a contact with phone number and optional name"""
    number: str
    name: str = ""


# ==============================================
#                  VALIDATOR                   
# ==============================================
class Validator:
    """Handles validation logic for contacts"""
    
    @staticmethod
    def validate_indian_number(number: str) -> bool:
        """Validates 10-digit Indian phone numbers starting with 6-9"""
        return re.match(r'^[6789]\d{9}$', str(number))


# ==============================================
#              WHATSAPP CONTROLLER             
# ==============================================
class WhatsAppAutomation:
    """Handles all WhatsApp desktop automation operations"""
    
    def __init__(self):
        self.wa_delay = 1  # Base delay between actions (seconds)
    
    def maximize_window(self, window_title: str = "WhatsApp") -> bool:
        """Maximizes the specified window (Windows only)"""
        try:
            if platform.system() == 'Windows':
                import win32gui
                window = win32gui.FindWindow(None, window_title)
                if window:
                    win32gui.ShowWindow(window, 3)  # SW_MAXIMIZE
                    time.sleep(0.5)
                    return True
            return False
        except Exception as e:
            print(f"[ERROR] Maximizing window: {e}")
            return False
    
    def launch_whatsapp(self) -> bool:
        """Launches and maximizes WhatsApp desktop app"""
        try:
            # Open WhatsApp via Windows search
            pyautogui.press('win')
            time.sleep(self.wa_delay)
            pyautogui.write('whatsapp')
            time.sleep(self.wa_delay)
            pyautogui.press('enter')
            time.sleep(0.5)  # Wait for app to launch
            
            # Ensure window is maximized
            return self.maximize_window()
        except Exception as e:
            print(f"[ERROR] Launching WhatsApp: {e}")
            return False
    
    def send_single_message(self, contact: Contact, message: str) -> bool:
        """Sends message to a single contact"""
        try:
            # Clear previous search
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.3)
            pyautogui.press('backspace')
            
            # Search for contact
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(self.wa_delay)
            pyautogui.write(contact.number)
            time.sleep(self.wa_delay)
            
            # Select contact and send message
            pyautogui.press('down')
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(0.5)
            
            pyautogui.write(message)
            time.sleep(0.5)
            pyautogui.press('enter')
            
            return True
        except Exception as e:
            print(f"[ERROR] Sending to {contact.number}: {e}")
            return False
    
    def minimize_whatsapp(self) -> bool:
        """Minimizes the WhatsApp window"""
        try:
            pyautogui.hotkey('win', 'down')
            return True
        except Exception as e:
            print(f"[ERROR] Minimizing WhatsApp: {e}")
            return False


# ==============================================
#               MAIN APPLICATION               
# ==============================================
class WhatsAppSender:
    """Main controller for WhatsApp messaging automation"""
    
    def __init__(self):
        self.validator = Validator()
        self.whatsapp = WhatsAppAutomation()
    
    def process_contacts(self, contacts: List[Contact], message: str) -> None:
        """Processes all contacts and sends messages sequentially"""
        total_contacts = len(contacts)
        print(f"\n Starting WhatsApp automation for {total_contacts} recipients...")
        
        if not self.whatsapp.launch_whatsapp():
            print("[ABORT] Failed to launch WhatsApp")
            return
        
        for index, contact in enumerate(contacts, 1):
            # Validate contact number
            if not self.validator.validate_indian_number(contact.number):
                print(f"X  Invalid number format: {contact.number}")
                continue
            
            # Send message
            print(f"\n Processing {index}/{total_contacts}: {contact.name or contact.number}")
            if self.whatsapp.send_single_message(contact, message):
                print("✓ Message sent successfully")
            else:
                print("X Failed to send message")
            
            # Add delay between messages (except last one)
            if index < total_contacts:
                print(f"⏳ Waiting 3 seconds before next message...")
                time.sleep(3)
        
        # Clean up
        self.whatsapp.minimize_whatsapp()
        print("\n Finished processing all contacts!")


# ==============================================
#               EXAMPLE USAGE                  
# ==============================================
if __name__ == "__main__":

    # Sample contact list
    
    demo_contacts = [
        Contact(number="8317384966"),
        Contact(number="9141823533")
       ]

    # Sample message
    demo_message = "Hello! This is an automated message from Python."
    
    
    # Initialize and run
    bot = WhatsAppSender()
    bot.process_contacts(
        contacts=demo_contacts,
        message=demo_message
    )