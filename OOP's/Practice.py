class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def welcome():
        print("Welcome to ABC")

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hii", self.name, "your average is", sum / len(self.marks))

s1 =  Student("Rahul", [30,30,10,30 ,30])
s1.welcome()
s1.avg()