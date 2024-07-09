#!/usr/bin/env python3

#try:
#    print(5 + 10)
#except TypeError:
#    print('At least one of the values is NOT an integer')

#try:
#    print(5 + 'ten')
#except TypeError:
#    print('At least one of the values is NOT an integer')

#try:
#    f = open('filethatdoesnotexist', 'r')
#    f.write('hello world\n')
#    f.close()
#except FileNotFoundError:
#    print('no file found')

#try:
#    f = open('filethatdoesnotexist', 'r')
#    f.write('hello world\n')
#    f.close()
#except (FileNotFoundError, PermissionError, IsADirectoryError): 
#    print('failed to open file')

try:
    f = open(abc, 'r')
    f.write('hello world\n')
    f.close()
except (FileNotFoundError, PermissionError): 
    print('file does not exist or wrong permissions')
except IsADirectoryError:
    print('file is a directory')
except OSError:
    print('unable to open file')
except:
    print('unknown error occured')
    raise