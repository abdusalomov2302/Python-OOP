class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-kurs talabasi.")


student = Student("Sevara", 20, 3)

student.info()