###
# Program that allows you to convert time in 24-hour format to 12-hour format
#
import time

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

if hour == 0:
    period = "AM"
    hour_12 = 12
elif 1 <= hour < 12:
    period = "AM"
    hour_12 = hour
elif hour == 12:
     period = "PM"
     hour_12 = hour
else: 
    period = "PM"
    hour_12 = hour - 12 

print(f'Enter time (24-hour format) {hour}:{minute}')
print(f'Time in 12-hour format: {hour_12}:{minute} {period}')

