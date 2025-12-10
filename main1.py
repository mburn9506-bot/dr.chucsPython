# handles opening and closing a file safely
with open ('notes.txt', 'w') as file:
        file.write("hello code pilot!")
with open('notes.txt','r') as file:
        content = file.read()
        print(content)

#appends text witout overwriting
with open('notres.txt','a') as file:
        file.write("\nanother line!")
with open('notes.txt','r') as file:
        content = file.read()
        print(content)

#read file line by line
with open('notes.txt','r') as file:
        for line in file:
                print(line.strip())
#read all lines into list
with open('notres.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

# saves a new line to a file
with open('notes.txt', 'a')as file:
        note = input("enter a note: ")
        file.write(f"\n{note}")

#reads and display all notes
with open('notes.txt','r')as file:
        print('yuor notes: ')
        for line in file:
                print(line.strip())

# clears the file content
with open('notes.txt', 'w')as file:
        file.write(" ")
# https://youtu.be/XX44XYjK_JQ?t=2902