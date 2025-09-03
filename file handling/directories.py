import os
# os.mkdir("directryi file")
print("this is 1st directy")
print("string format:",os.getcwd)
# os.rename("directryi file","DIRECTORIES")
print("file name changed directryi file to DIRECTORIES.")

print("The files are:",os.listdir())

print("Cheak name is directory or not:",os.path.isdir("D:\TY\Python\Dictionary.py"))

print("directory removed.",os.rmdir("DIRECTORIES"))