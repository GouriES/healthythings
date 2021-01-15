import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Drink Glass of Water.",
        message ="The correct way to drink water is to sit down with a glass of water, and drink it sip by sip. One should consume at least 2-3 litres of water in a day. Drinking room temperature water over very cold water should be preferred",
        app_icon="D:\\projt python\\pytho2\\exercise_07\\water.ico",
        timeout=5
        )
    time.sleep(20*60)

    notification.notify(
        title="Eyes Exercise.",
        message ="Hold your pointer finger a few inches away from your eye and look around.",
        app_icon="D:\\projt python\\pytho2\\exercise_07\\eyes.ico",
        timeout=5
        )
    time.sleep(40*60)

    notification.notify(
        title="Strech Your Body.",
        message ="Do little stretching with your moves.",
        app_icon="D:\\projt python\\pytho2\\exercise_07\\exercise.ico",
        timeout=5
        )
    time.sleep(20*60)











