#Python Program to Count Capital Letters in a File

with open("text.txt") as file:
    count = 0
    text = file.read()
    for i in text:
        if i.isupper():
            count += 1
    print(count)