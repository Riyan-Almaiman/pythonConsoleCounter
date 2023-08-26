import random
import time

data_list = [random.randint(0, 100) for number in range(1000)] #1000 random numbers from 1-100

# things you can log
things_to_be_logged = {
    'Numbers smaller than 3': lambda x: x < 3,
    'Numbers equal to 10': lambda x: x == 10,
    'Numbers smaller than 20': lambda x: x < 20,
    'Numbers between 20 and 50': lambda x: 20 <= x <= 50,
    'Numbers bigger than 50': lambda x: x > 50
}

log_counter = {}
log_indexes = []

print('Generating 1000 numbers and counting their values')

def update_counter(val, display_text):
    if display_text not in log_counter:
        log_counter[display_text] = 0
        log_indexes.append(display_text)

    line_num = log_indexes.index(display_text) + 1
    print(f'\r\033[{line_num}B', end='', flush=True)
    log_counter[display_text] += 1
    print(f'\r{display_text}: {log_counter[display_text]}', end='', flush=True)
    print(f'\r\033[{line_num}A', end='', flush=True)



for value in data_list:
    for display_text, condition in things_to_be_logged.items():
        if condition(value):
            update_counter(value, display_text)
            break
    time.sleep(.1)

input()
