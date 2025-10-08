class animal:
    def __init__(self):
        self.animal_name = input("category of animal: ")

    def show_project(self):
        print("animal Name:", self.animal_name)

class name(animal):
    def __init__(self):
        super().__init__()
        self.name_name = input("animal Name: ")

    def show_name(self):
        print("name Name:", self.name_name)


class action(name):
    def __init__(self):
        super().__init__()
        self.sound= input("sound of animal: ")
        

    def show_action(self):
        self.show_project()     
        self.show_name()      
        print("animal sound:", self.sound)



task_obj = action()
print("\n--- Details ---")
task_obj.show_action()