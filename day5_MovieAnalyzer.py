# Movie Rating Analyzer using OOP

class Movie:
    platform = "IMDb"  # class variable

    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self._rating = None
        self.rating = rating  # use setter

    # property getter
    @property
    def rating(self):
        return self._rating

    # property setter with validation
    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self._rating = value
        else:
            raise ValueError("Rating must be between 0 and 10")

    # class method to change platform
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

    # static method to check hit movie
    @staticmethod
    def is_hit(rating):
        return rating >= 8

    def __str__(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating}"


# -------------------------------
# Creating movie objects
# -------------------------------
movies = [
    Movie("Inception", "Sci-Fi", 8.8),
    Movie("Interstellar", "Sci-Fi", 8.6),
    Movie("Joker", "Drama", 8.4),
    Movie("The Room", "Drama", 3.7),
    Movie("Avengers", "Action", 7.9),
]

# -------------------------------
# Sort movies by rating (high to low)
# -------------------------------
movies_sorted = sorted(movies, key=lambda m: m.rating, reverse=True)

print("🎬 Movies sorted by rating:")
for movie in movies_sorted:
    print(movie)

# -------------------------------
# List comprehension: hit movies
# -------------------------------
hit_movies = [m for m in movies if Movie.is_hit(m.rating)]

print("\n🔥 Hit Movies:")
for movie in hit_movies:
    print(movie.title)

# -------------------------------
# Membership operator
# -------------------------------
search_title = "Inception"
titles = [m.title for m in movies]

if search_title in titles:
    print(f"\n✅ '{search_title}' exists in the movie list")
else:
    print(f"\n❌ '{search_title}' not found")

# -------------------------------
# Bonus: Genre-wise printing
# -------------------------------
print("\n🎭 Movies by Genre:")
genres = set(m.genre for m in movies)

for genre in genres:
    print(f"\n{genre}:")
    for movie in movies:
        if movie.genre == genre:
            print(f"  - {movie.title}")

# -------------------------------
# Bonus-ready: match-case menu (Python 3.10+)
# -------------------------------
def menu(choice):
    match choice:
        case 1:
            print("\nAll Movies:")
            for m in movies:
                print(m)
        case 2:
            print("\nHit Movies:")
            for m in hit_movies:
                print(m)
        case 3:
            Movie.change_platform("Rotten Tomatoes")
            print(f"\nPlatform changed to {Movie.platform}")
        case _:
            print("\nInvalid choice")


# Example menu call
menu(2)
