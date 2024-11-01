import time
my_time = int(input('Enter seconds you want to sleep: '))
for x in range(0, my_time):
    seconds = x % 60
    minutes = x // 60
    hours = minutes // 60
    print(f'{seconds}:{minutes}:{hours}')
    time.sleep(1)
print('WAKE UP')