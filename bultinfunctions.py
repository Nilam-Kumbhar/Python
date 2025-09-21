class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects  

    def show(self):
        print("Name:", self.name)
        print("Subjects:", self.subjects)
        print("Total Subjects:", len(self.subjects))

obj = Student("Nilam", ["Math", "Science", "Python"])
obj.show()
