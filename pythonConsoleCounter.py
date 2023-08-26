import random
import time

data_list = [random.randint(0, 100) for number in range(1000)] #random numbers to use
thingsToBeLogged = ['less than 20', 'less than 50', 'greater than 50'] ## useless in this situation
counter_dictionary = {}
order_of_logs = []

print('Generating 1000 numbers and counting their values')
def update_counter(val, display_text):

    if display_text not in counter_dictionary:
        counter_dictionary[display_text] = 0
        order_of_logs.append(display_text)

    line_num = order_of_logs.index(display_text) + 1
    print(f'\r\033[{line_num}B', end='', flush=True)
    counter_dictionary[display_text] += 1
    print(f'\r{display_text}: {counter_dictionary[display_text]}', end='', flush=True)
    print(f'\r\033[{line_num}A', end='', flush=True)

for value in data_list:
    
    if value < 3:
        update_counter(value, 'Numbers smaller than 3')
    elif value == 10:
        update_counter(value, 'Numbers equal to 10')
    elif value < 20:
        update_counter(value, 'Numbers smaller than 20')    
    elif 20 <= value <= 50:
        update_counter(value, 'Numbers between 20 and 50')
    else:
        update_counter(value, 'Numbers bigger than 50')
    time.sleep(.1)

input()
