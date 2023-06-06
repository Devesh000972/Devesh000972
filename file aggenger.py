import os

i = 0  # initialize the counter to 0
a = [f for f in os.listdir() if f.endswith('.png')]  # list all .txt files in the current directory
b = len(a)  # get the length of the list

while i < b:  # loop until the counter reaches the length of the list
    old_name = a[i]  # get the current filename
    new_name = str(i) + '.png'  # generate the new filename
    os.rename(old_name, new_name)  # rename the file
    i += 1  # increment the counter
