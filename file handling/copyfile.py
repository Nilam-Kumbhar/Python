f = open("sample.txt", "r")
content = f.read()
f.close()

f2 = open("copy_sample.txt", "w")
f2.write(content)
f2.close()

print("File copied successfully!")