student_marks = {
    "Alice": 74,
    "Bob": 92,
    "Charlie": 78,
    "David": 65,
    "Eve": 90
}
student_name_input = input("Enter the student's name: ")
if student_name_input in student_marks:
     marks = student_marks[student_name_input]
     print(f"{student_name_input}'s marks: {marks}")
else:
    print("Student not found.")