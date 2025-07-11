class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title 
        self.genre = genre
        self.duration = duration
        self.rating = rating


    def show_summary(self):
        print(f"{self.title} - {self.genre}dagi film. {self.rating}/10.")

movie = Movie("Qasoskorlar4:(Imtiho)", "Daxshatli janr", 181, 9.5)


movie.show_summary()