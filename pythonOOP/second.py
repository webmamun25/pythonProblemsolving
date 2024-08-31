class SchoolManagement:

    def __init__(self):
        print(id(self))
        self.user_name=input("Enter your name:")

        self.user_id=input("Enter your id:")
        self.Student()
    def Student(self):
        print("Hello",self.user_name)


obj=SchoolManagement()

print(id(obj))