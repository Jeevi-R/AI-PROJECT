import winsound
import threading
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
alarm_path = os.path.join(BASE_DIR, "resources", "alarm.wav")
alarm_on = False

def play_alarm():
    global alarm_on
    while alarm_on:
        winsound.PlaySound(alarm_path, winsound.SND_FILENAME)

def start_alarm():
    global alarm_on
    if not alarm_on:
        alarm_on = True
        threading.Thread(target=play_alarm, daemon=True).start()

def stop_alarm():
    global alarm_on
    alarm_on = False
    winsound.PlaySound(None, winsound.SND_PURGE)