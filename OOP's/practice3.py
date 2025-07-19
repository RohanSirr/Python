class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy) / 3) + "%"

stu1 = Student(98,95,97)
print(stu1.percentage) # Output: 96.66666666666667%
stu1.phy = 34
print(stu1.percentage) # Output: 73.33333333333333%