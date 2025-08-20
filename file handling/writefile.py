file=open('sample.txt',"x")
print("file created.")

file=open('sample.txt',"w")
file.write("Hello, this is my first file.\n")
file.write("File handling in Python is easy!")

file = open("sample.txt", "a")
file.write("\nThis line is added later.\n")

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

with open("demo.txt", "w") as f:
    f.write("Python file handling example.\n")
    f.write("This is line 2.\n")

with open("demo.txt", "a") as f:
    f.write("This line is appended.\n")

with open("demo.txt", "r") as f:
    print("File content:\n", f.read())