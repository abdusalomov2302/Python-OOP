
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        print(f"{self.title} - {"O'qilgan" if self.is_read else "O'qilmagan"}")


books = [
    Book("Sehrli qalpoqcha", "Xudoyberdi To'xtaboyev"),
    Book("Boy ota, kambag'al ota", "Robert Kiyosaki"),
    Book("Ufq", "Tog'ay Murod"),
    Book("Dunyoning ishlari", "O'tkir Hoshimov"),
    Book("Ikki eshik orasi", "Erkin A'zam")
]

books[1].mark_as_read()
books[4].mark_as_read()

print("Kitoblar:")
for b in books:
    b.status()

print("O'qilgan kitoblar:")
for b in books:
    if b.is_read:
        print("-", b.title)