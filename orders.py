#We are using open(), built in function from python to open files.

def open_and_print(file_to_open):
    try:
        file = open(file_to_open, 'r')
        file_line_list = file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        file.close()
    except FileNotFoundError as errmsg:
        print("Hi! File could not be open, please see below:")
        print(errmsg)

open_and_print('order.txt')

