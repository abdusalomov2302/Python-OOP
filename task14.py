class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Ismi: {self.name}, Yoshi: {self.age}")


student1 = Student("Sevara", 20, 5)
student2 = Student("Jasur", 22, 4)
student3 = Student("Madina", 19, 3)
student4 = Student("Alisher", 25, 4)
student5 = Student("Dilshod", 21, 5)

students = [student1, student2, student3, student4, student5]

oldest_student = max(students, key=lambda s: s.age)

print("Eng katta yoshdagi student:")
oldest_student.show_info()