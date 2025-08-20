file=open('myfile.txt',"w+")
file.write("Hello, this is my first file.\n")
file.seek(6)
print(file.read())
file.seek(6)
file.write("universe")

print(file.tell())
