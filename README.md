🔑 𝑪𝒓𝒐𝒔𝒔-𝑷𝒍𝒂𝒕𝒇𝒐𝒓𝒎 𝑲𝒆𝒚𝒍𝒐𝒈𝒈𝒆𝒓 (𝑬𝒅𝒖𝒄𝒂𝒕𝒊𝒐𝒏𝒂𝒍 𝑼𝒔𝒆 𝑶𝒏𝒍𝒚)


⚠️ 𝐃𝐢𝐬𝐜𝐥𝐚𝐢𝐦𝐞𝐫:
This script is for educational purposes only. Do not use it for malicious purposes. Monitoring someone else's device without their consent is illegal and unethical. Always ensure compliance with local laws and regulations.

📋 𝑷𝒓𝒆𝒓𝒆𝒒𝒖𝒊𝒔𝒊𝒕𝒆𝒔

Before running the script, install the required Python library:

pip install pynput


Save the script as a .py file (e.g., keylogger.py).

🖥️ 𝐇𝐨𝐰 𝐈𝐭 𝐖𝐨𝐫𝐤𝐬
𝙆𝙚𝙮 𝘿𝙚𝙩𝙚𝙘𝙩𝙞𝙤𝙣 𝙖𝙣𝙙 𝙇𝙤𝙜𝙜𝙞𝙣𝙜

• Uses the pynput library to monitor key presses.

• The on_press function is triggered on every keystroke.

• Keys are logged as strings into a file named 𝘬𝘦𝘺𝘭𝘰𝘨.𝘵𝘹𝘵 in the script’s directory.

• Each key press is written on a new line (e.g., 'a', 'b', 'Key.space').

💻 𝑪𝒓𝒐𝒔𝒔-𝑷𝒍𝒂𝒕𝒇𝒐𝒓𝒎 𝑺𝒖𝒑𝒑𝒐𝒓𝒕

• The script runs on Windows and Linux.

• It uses sys.platform to detect the OS.

• No OS-specific code is needed for key listening due to pynput’s abstraction over Windows API and X11/evdev.

🕵️ 𝑹𝒖𝒏𝒏𝒊𝒏𝒈 𝒕𝒉𝒆 𝑺𝒄𝒓𝒊𝒑𝒕 𝑺𝒊𝒍𝒆𝒏𝒕𝒍𝒚

𝑾𝒊𝒏𝒅𝒐𝒘𝒔

• Use 𝙥𝙮𝙩𝙝𝙤𝙣𝙬.𝙚𝙭𝙚 to run the script without a console window:

pythonw keylogger.py


• The script hides the console window using ctypes for stealth.

𝑳𝒊𝒏𝒖𝒙

 • you can either make a virtual enviroment: 

pytohn3 -m venv venv

source venv/bin/activate

• or,alternatively you can run it directly: 

pip install pynput --break-system-packages

• Run the script in the background using:

python3 keylogger.py &


• Or detach it from the terminal using:

nohup python3 keylogger.py &


𝐍𝐨𝐭𝐞: It requires a graphical environment (e.g., X11). May not work in headless or TTY sessions.

⚠️ 𝑳𝒊𝒎𝒊𝒕𝒂𝒕𝒊𝒐𝒏𝒔 & 𝑾𝒂𝒓𝒏𝒊𝒏𝒈𝒔

𝑷𝒆𝒓𝒎𝒊𝒔𝒔𝒊𝒐𝒏𝒔:

• May require administrative/root privileges.

• Could be blocked or flagged by antivirus software.

𝑫𝒆𝒕𝒆𝒄𝒕𝒊𝒐𝒏:

• This script is not stealthy and is easily detectable by modern security tools.

𝑬𝒏𝒗𝒊𝒓𝒐𝒏𝒎𝒆𝒏𝒕:

On Linux, may fail outside of a graphical session.

Additional dependencies like python3-xlib might be required.

𝑳𝒐𝒈𝒈𝒊𝒏𝒈:

• Logs are stored in 𝙠𝙚𝙮𝙡𝙤𝙜.𝙩𝙭𝙩 in the same directory.

• Ensure the script has write permissions.

• Stopping the Script:

• Manually terminate the process:

• 𝗪𝗶𝗻𝗱𝗼𝘄𝘀: Task Manager

• 𝗟𝗶𝗻𝘂𝘅: 𝙥𝙨 + 𝙠𝙞𝙡𝙡 command
