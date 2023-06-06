from plyer import notification
import time
import datetime

def my_func():
    # your code here
    # Set up notification parameters
    title = "Water drinking remainder"
    message = "Drint water every day to bealive"
    app_icon = None  # insert path to your app icon here
    timeout = 10  # notification timeout in seconds
    # Send notification
    notification.notify(title=title, message=message, app_icon=app_icon, timeout=timeout)
    

while True:
    now = datetime.datetime.now()
    if now.hour % 2 == 0 and now.minute == 0:
        my_func()
    time.sleep(60)
