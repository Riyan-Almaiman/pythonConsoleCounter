import time

data_list = [1,2,1,4,5,14,14,5,14,5,14,2,1,2,1,5,14,5,14,3,2,4,5,14,5,14,5,14,4,5,14,5,14,5,14,2,12,12,2,1,2,1,2,1,2,1,2,1,15,14,5,14,5,14,5,14,5,14,5,14,5,14,5,14,5,15,14,5,14,5,1,9,8,3,2,4]  # shortened for brevity
thingsToBeLogged = ['less than 3', 'less than 5', 'greater than 9'] ## useless in this situation
counter_dictionary = {}
order_of_logs = []

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
        update_counter(value,'less than 3')
    elif 3 <= value <= 5:
        update_counter(value, 'less than 5')
    else:
        update_counter(value, 'greater than 5')
    time.sleep(.1)

input()
