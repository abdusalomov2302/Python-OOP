
class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active


student = User("Sevara", "sevara23@gmail.com", False)

print(student.username)
print(student.email)
print(student.is_active)