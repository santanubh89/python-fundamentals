import time

current_time = time.ctime()
print(f'Current time: {current_time}')

seconds_since_1970 = time.time()
print(f'Seconds elapsed since 1970: {seconds_since_1970}')
print(f'Days elapsed since 1970: {seconds_since_1970/(60*60*24)}')

local_time = time.localtime()
formatted_time = time.strftime('%H:%M:%S %p', local_time)
print(f'Year: {local_time.tm_year}, Month: {local_time.tm_mon}, Day: {local_time.tm_mday}')
print(f'Formatted Local time: {formatted_time}')