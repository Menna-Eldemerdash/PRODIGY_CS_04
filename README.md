# PRODIGY_CS_04
This Python script is a keylogger that captures and logs all the keystrokes typed on a keyboard. The logged data is stored in a text file for further analysis. This script demonstrates how to use the pynput library for handling keyboard events.

Disclaimer: This code is for educational purposes only. Unauthorized use of keyloggers may violate privacy laws and regulations. Always obtain proper consent before using.

How the Code Works
1. Library Import
The script uses the pynput library, which is a Python module for controlling and monitoring input devices like the keyboard and mouse.
Specifically, it imports:
Key: To identify special keys like Space, Enter, and Backspace.
Listener: To listen for keyboard events (key presses).
2. Log File Setup
The LOG_FILE variable specifies the name of the file where the logged keystrokes will be stored (keylog.txt).
All keystrokes are appended to this file during execution.
3. Logging Functionality
The function log_key(key) handles the process of saving each keystroke to the file:

It opens the log file in append mode ("a") to ensure new data is added without overwriting the file.
Key Handling:
Normal Keys:
For standard alphanumeric keys, key.char is used to capture the character pressed.
Special Keys:
Keys like Space, Enter, and Backspace are replaced with readable labels:
[SPACE] for spaces
[ENTER] for the Enter key
[BACKSPACE] for the Backspace key
Any other special keys (e.g., Shift, Ctrl) are captured using str(key).
4. Keyboard Listener
The Listener class from pynput.keyboard monitors keyboard activity.
The on_press event is used to log each key as soon as it is pressed.
The listener.join() method keeps the script running in the background, listening for keystrokes indefinitely.
5. Main Function
The main() function initializes the Listener and starts logging keyboard activity.
When executed, the script begins capturing and logging keystrokes to the keylog.txt file.
6. Execution Block
The if __name__ == "__main__": block ensures that the main() function is executed only when the script is run directly, not when imported as a module.
How to Use
Requirements:

Python 3.x
pynput library (install it using pip install pynput).
Running the Script:

Save the script as keylogger.py.
Run the script in a terminal or IDE:
Copy code
python keylogger.py
Log File:

The keystrokes will be saved in a file named keylog.txt in the same directory as the script.
Example Output in keylog.txt
When typing the text "Hello World!" followed by pressing Enter:

css
Copy code
 H e l l o  [SPACE] W o r l d !  [ENTER]
Warnings and Legal Notice
Purpose: This script is for educational and ethical hacking purposes only.
Ethics: Using keyloggers without explicit permission is illegal and unethical. Use this script responsibly and only with appropriate consent.
