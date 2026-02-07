#Basic Alarm Clock – Set a time, and the program plays a sound when it reaches that time
import datetime
import time
import os

from playsound import playsound

def alarm_clock(alarm_time,song):
    print(f"Alarm is set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("⏰ Wake up! Alarm time!")
            playsound(song)
            break
        time.sleep(10)  


alarm_time = input("Enter alarm time in HH:MM format (24-hour): ")
song="fire_alarm.mp3"
alarm_clock(alarm_time, song)

