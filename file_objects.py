# unsing the open method we are obligated to explicitly close the file programmatically
f = open('test.txt'. 'r')

# leaks? maximum allowed file descriptors?
f.close() 

# a context manager allows us to work with files inside the block so if we exit that block the file is closed automatically
with open('text.txt', 'r') as f:

