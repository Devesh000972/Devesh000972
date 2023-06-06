import time
import datetime
import os
from plyer import notification

try:
    # Attempt to import the necessary pyobjc modules on macOS
    if os.name == "posix":
        import Foundation
        import AppKit
except ImportError:
    # If pyobjc is not installed on macOS, prompt the user to install it
    if os.name == "posix":
        print("The pyobjc package is required to run this script on macOS.")
        print("Please install it using the command: pip install pyobjc")
        exit()

def my_func():
    # your code here
    title = "Water drinking remainder"
    message = "Drink water every day to believe"
    app_icon = None
    timeout = 10
    
    if os.name == "nt":
        # Use a Windows-specific app icon
        app_icon = "path/to/windows/icon.ico"
        # Set a custom notification timeout
        timeout = 5
    elif os.name == "posix":
        if sys.platform == "darwin":
            # Use a macOS-specific app icon
            app_icon = "path/to/macos/icon.png"
        elif "linux" in sys.platform:
            # Use a Linux-specific app icon
            app_icon = "path/to/linux/icon.png"

    # Send notification
    notification.notify(title=title, message=message, app_icon=app_icon, timeout=timeout)
    
while True:
    now = datetime.datetime.now()
    if now.hour % 2 == 0 and now.minute == 0:
        my_func()
    time.sleep(60)
