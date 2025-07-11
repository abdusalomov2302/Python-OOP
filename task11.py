class Book:
    def __init__(self, title, auther, is_read):
        self.title = title
        self.author = auther
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o'qilgan")

    def status(self):
        if self.is_read:
            print("o'qildi")
        else:
            print("o'qilmagan")


book = Book("Sehrli qalpoqcha", "Xudoyberdi To'xtaboyev", False)

book.status()

book.mark_as_read()

book.status()