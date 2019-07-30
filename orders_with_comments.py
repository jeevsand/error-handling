# We are using open(), built in function from python to open files.

# try:        #tries to run the block of code
#     file = open('order.txt', 'r')
# except:     #if it fails then it runs this block of code
#     print("File could not be open")

try:  # tries to run the block of code
    file = open('order.txt', 'r')
    file_line_list = file.readlines()
    print(type(file_line_list))
    for line in file_line_list:
        print(line.rstrip('\n'))

    file.close()  # if you dont close it you can cause a lock in the file - similar to trying to delete a file that is open.
except FileNotFoundError as errmsg:  # if it fails then it runs this block of code
    print("Hi! File could not be open, please see below:")
    print(errmsg)
    raise  # sends the default error and stops the code