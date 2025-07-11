class Book:
    def __init__(self, title, auther, is_read):
        self.title = title
        self.author = auther
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o'qilgan")

    def status(self):
        x = "Oqilgan" if self.is_read else "Oqilmagan"
        print(f"{self.title} - {x}")


book1 = Book("Sehrli qalpoqcha", "Xudoyberdi To'xtaboyev",True)
book2 = Book("Dunyoning ishlari", "O'tkir Hoshimov", True)
book3 = Book("Ufq", "Tog'ay Murod", False)
book4 = Book("Boy ota, kambag'al ota", "Robert Kiyosaki", False)

book1.mark_as_read()
book2.mark_as_read()

book1.status()
book2.status()
book3.status()
book4.status()