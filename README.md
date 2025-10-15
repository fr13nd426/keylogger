# Assignment🔑 Cross-Platform Keylogger (Educational Use Only)

⚠️ Disclaimer:
This script is for educational purposes only. Do not use it for malicious purposes. Monitoring someone else's device without their consent is illegal and unethical. Always ensure compliance with local laws and regulations.

📋 Prerequisites

Before running the script, install the required Python library:

pip install pynput


Save the script as a .py file (e.g., keylogger.py).

🖥️ How It Works
Key Detection and Logging

Uses the pynput library to monitor key presses.

The on_press function is triggered on every keystroke.

Keys are logged as strings into a file named keylog.txt in the script’s directory.

Each key press is written on a new line (e.g., 'a', 'b', 'Key.space').

💻 Cross-Platform Support

The script runs on Windows and Linux.

It uses sys.platform to detect the OS.

No OS-specific code is needed for key listening due to pynput’s abstraction over Windows API and X11/evdev.

🕵️ Running the Script Silently
Windows

Use pythonw.exe to run the script without a console window:

pythonw keylogger.py


The script hides the console window using ctypes for stealth.

Linux

Run the script in the background using:

python keylogger.py &


Or detach it from the terminal using:

nohup python keylogger.py &


Note: It requires a graphical environment (e.g., X11). May not work in headless or TTY sessions.

⚠️ Limitations & Warnings

Permissions:

May require administrative/root privileges.

Could be blocked or flagged by antivirus software.

Detection:

This script is not stealthy and is easily detectable by modern security tools.

Environment:

On Linux, may fail outside of a graphical session.

Additional dependencies like python3-xlib might be required.

Logging:

Logs are stored in keylog.txt in the same directory.

Ensure the script has write permissions.

Stopping the Script:

Manually terminate the process:

Windows: Task Manager

Linux: ps + kill command
