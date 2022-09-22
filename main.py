from playsound import *
from datetime import *

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Неверный формат, попробуйте еще раз.'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный формат часов, попробуйте еще раз.'
        elif int(alarm_time[3:5]) > 59:
            return 'Неверный формат минут, попробуйте еще раз.'
        elif int(alarm_time[6:8]) > 59:
            return 'Неверный формат секунд, попробуйте еще раз'
        else:
            return 'Отлично!'

while True:
    alarm_time = input('Введите время в следующем формате \'HH:MM:SS\' \nВремя будильника')