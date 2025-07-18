class Student:
    
    college_name = "Lovely Professional University"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def welcome(self):
        print(f"Welcome, {self.name} to {self.college_name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

s1 = Student("Rohan", 20, 10)
s1.welcome()
