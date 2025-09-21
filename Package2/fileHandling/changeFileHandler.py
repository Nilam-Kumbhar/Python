
def read11Line(filename):
    with open(filename, "r") as f:
      
        lines = f.readlines()

    
    with open("file3.txt", "a") as file3:
        for line in lines[10:]:
            file3.write(line)



