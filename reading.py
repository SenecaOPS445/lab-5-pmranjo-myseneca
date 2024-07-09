#!/usr/bin/env python3

f = open('data.txt', 'r')

f.read()            # read the entire contents and return a single string object
f.readlines()       # read the entire contents and return each line in the file as a list
f.readline()        # return the first line, if run a second time it will return the second line, then third
f.close()           # close the opened file

#read_data = f.read()

#f.close()                               # This method will close the file

#f = open('data.txt', 'r')               # Open file
#read_data = f.read()                    # Read from file
#print(read_data)
#f.close()                               # Close file

# METHOD 1:

#f = open('data.txt', 'r')
#method1 = list(f)
#f.close()
#print(method1)

# METHOD 2:

f = open('data.txt', 'r')
method2 = f.read()
f.close()
print(method2)