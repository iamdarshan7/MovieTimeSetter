from datetime import datetime
from playsound import playsound

# Enter numbers in double digits like 03:01:45 PM
alarm_time = input('Enter the time of alarm to be set:HH:MM:SS\n')
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print('Setting up alarm..')

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime('%S')
    current_period = now.strftime("%p")
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):
                    break

print("It's movie time, Dude!!!")
print('Grab your popcorn and enjoy Dude!!!')
# place your movie in the same directory to this file
playsound('write_your_movie_fileName_with.extension_here')
