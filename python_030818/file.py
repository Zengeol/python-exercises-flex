file_handle = open('hello.txt', 'w')
file_handle.write('Hello World\n')
file_handle = open('hello2.txt', 'w')
file_handle.write('Hello World2\n')
file_handle.close()

file_handle = open('hello.txt', 'r')
contents = file_handle.read()
file_handle.close()
print(contents)

file_handle = open('hello.txt', 'r')
contents = file_handle.readlines()
file_handle.close()
print(contents)
file_handle = open('hello.txt', 'r')
line1 = file_handle.readline()
file_handle.close()
print(line1)

file_handle = open('hello.txt', 'r')
while True:
    char = file_handle.read(1)
    if not char:
        break
    
    else:
        print(char)
file_handle.close()

file_handle = open('hello.txt', 'a')
file_handle.close()

import io
file_handle = io.StringIO()
file_handle.write("Some more stuff")
contents = file_handle.getvalue()
file_handle = io.StringIO("initial text")
contents = file_handle.read()
print(contents)
file_handle.close()