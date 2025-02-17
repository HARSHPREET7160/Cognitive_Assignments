#7.1
with open('file_test.txt', 'w') as file:
    file.write('Hello, this is a sample text.')
    
with open('file_test.txt', 'r') as file:
    content = file.read()
    print(content)
    
#7.2
with open('file_test.txt', 'a') as file:
    file.write('This is the appended text.')
    
with open('file_test.txt', 'r') as file:
    content = file.read()
    print(content)
    
#7.3
with open('file_test.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print("Number of lines in the file:", line_count)