# time
time_in_seconds = int(input('Enter tome in seconds: '))
if time_in_seconds <= 86400:
    time = '{time_in_seconds//3600:02}:{time_in_seconds // 60 % 60:02}:{time_in_seconds % 60:02}'
    print(f'time {time}.')
