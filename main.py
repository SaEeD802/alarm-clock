from playsound import playsound
from datetime import datetime

alarm_time = input("Enter Alam Time (HH:MM): ") #12:13
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]

print("Alarm set shod, Bro bekhab :)")

while True:
    now = datetime.now()
    c_hour = now.strftime("%H")
    c_minute = now.strftime("%M")

    if alarm_hour == c_hour and alarm_minute == c_minute:
        playsound("alarm.mp3")
        print("Boland Shoooooo :)")
        break
        