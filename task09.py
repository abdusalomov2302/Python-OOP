class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print(f"{self.username} faol(aktiv)")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} bloklandi!")


student = User("Sevara", "sevara23@gmail.com", False)


student.activate()
student.deactivate()