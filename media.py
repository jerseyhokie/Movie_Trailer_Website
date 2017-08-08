import webbrowser

class Movie():
    """ This class provides a way to store a movies related information

    Attributes:
        title: A string of the movies title
        storyline: A string of the movies main storyline or description
        poster_image_url: A string containing the movies poster via IMDB
        trailer_youtube_url: A string to the best quality trailer for the movie on YouTube
        VALID_RATINGS: a string of the movies rating - G, PG, PG-13 or R

    Functions:
        All attributes can be displayed with show_[Attribute Name] function calls
    
    """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
        """ Inits Movie with all required attributes """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.VALID_RATINGS = rating

    def show_title(self):
        """ Print the title """
        print self.title

    def show_storyline(self):
        """ Print the storyline """
        print self.storyline

    def show_poster(self):
        """ Open a webbrowser window with the movie poster """
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        """ Open a webbrowser window with the movie trailer """
        webbrowser.open(self.trailer_youtube_url)    

    def show_rating(self):
        """ Print the rating """
        print self.VALID_RATINGS
