import random
import time

def update_counter(val, log_text):
    if log_text not in log_counter:
        log_counter[log_text] = 0
        log_indexes.append(log_text)

    line_num = log_indexes.index(log_text) + 1
    print(f'\r\033[{line_num}B', end='', flush=True)
    log_counter[log_text] += 1
    print(f'\r{log_text}: {log_counter[log_text]}', end='', flush=True)
    print(f'\r\033[{line_num}A', end='', flush=True)


data_list = [random.randint(0, 100) for number in range(1000)] #1000 random numbers from 0-100

# things you can log
things_to_be_logged = {
    'Numbers smaller than 3': lambda x: x < 3,
    'Numbers equal to 10': lambda x: x == 10,
    'Numbers smaller than 20': lambda x: x < 20,
    'Numbers between 20 and 50': lambda x: 20 <= x <= 50,
    'Numbers bigger than 50': lambda x: x > 50
}

log_counter = {}
log_indexes = [] # keep track of the order of when something was logged to update the correct line


print('Generating 1000 numbers and counting their values')

for value in data_list:
    for log_text, condition in things_to_be_logged.items():
        if condition(value):
            update_counter(value, log_text)
    time.sleep(.1)

input()
