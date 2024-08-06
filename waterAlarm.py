import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Ronak its time to drink",
            message = "Stay hydrated Ronak, Hottest summer is here, Keep creating like me"
        )
        time.sleep(60*60)