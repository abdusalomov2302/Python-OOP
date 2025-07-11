
class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

movie = Movie("Qasoskorlar4:(Imtiho)", "Daxshatli film", 181, 9.5)

print("Kino nomi:", movie.title)
print("Janri:", movie.genre)
print("Davomiyligi (daqiqa):", movie.duration)
print("IMDB reytingi:", movie.rating)