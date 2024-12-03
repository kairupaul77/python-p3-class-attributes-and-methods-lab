class Song:
    # Class attributes to keep track of the count, genres, artists, and genre/artist counts
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Constructor to initialize song attributes and update class-level data."""
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count whenever a new song is created
        Song.add_song_to_count()

        # Add the genre and artist to their respective class attributes
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Add to genre and artist count histograms
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a new genre to the genres list, ensuring no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds a new artist to the artists list, ensuring no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre count histogram."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist count histogram."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Test case to validate functionality
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Hotline Bling", "Drake", "Pop")
song3 = Song("Run the World", "Beyonce", "Pop")
song4 = Song("99 Problems", "Jay-Z", "Rap")

# Output the results
print("Total song count:", Song.count)  # Output the number of songs
print("Artists:", Song.artists)  # Output all artists
print("Genres:", Song.genres)  # Output all genres
print("Genre count histogram:", Song.genre_count)  # Output genre count histogram
print("Artist count histogram:", Song.artist_count)  # Output artist count histogram
