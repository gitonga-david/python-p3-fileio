# opening a file
text_file = open("lib/filename.txt")

# a file should be closed as soon as we are thro with it
text_file.close()

# alternatively, we can use the with statement
with open("lib/filename.txt") as text_file:
    # do something with the file
    text_file.read()

# mode 
# r - read
# w - write - if the file already exists and we use tis mode the file will be overwritten
# a - append

# What can we do with opened files? The default mode is read

