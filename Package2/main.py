from fileHandling import fileRead,fileWrite,fileUpdate,changeFileHandler

file1=input("Enter Name of file 1:")

content1=fileRead.readFile(file1)
file2=input("Enter Name of file 2:")
content2=fileRead.readFile(file2)

file3=input("Enter name of file in which you want to write content")
fileWrite.writeFile(file3,content1)
fileWrite.writeFile(file3,content2)

changeFileHandler.read11Line("file4.txt")

updateFile=input("Enter name of file to update content")

updatedContent=input("Enter new Content")
fileUpdate.update(updateFile,updatedContent)
