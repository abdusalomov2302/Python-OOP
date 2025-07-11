class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("Sevara", 20, 5)
student2 = Student("Sevinch", 17, 4)
student3 = Student("Sarvinoz", 21, 3)

print(student1.name)
print(student2.age)
print(student3.grade)