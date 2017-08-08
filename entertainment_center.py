import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "PG-13")

bird_cage = media.Movie("The Bird Cage",
                        "A drag star and his husband host the conservative"
                        " parents of their sons fiance",
                        "https://upload.wikimedia.org/wikipedia/en/7/76/Birdcage_imp.jpg",
                        "https://www.youtube.com/watch?v=MxfXR1zSj1k",
                        "R")

star_wars = media.Movie("Star Wars",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky "
                        "pilot, a Wookiee, and two droids to save the galaxy from "
                        "the Empire's world-destroying battle-station, while also "
                        "attempting to rescue Princess Leia from the evil Darth Vader.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "PG")
                        
the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about "
                         "the true nature of his reality and his role in the "
                         "war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=ItH3RpObRHQ",
                         "R")

the_fifth_element = media.Movie("The Fifth Element", 
                                "In the colorful future, a cab driver unwittingly "
                                "becomes the central figure in the search for a "
                                "legendary cosmic weapon to keep Evil and Mr "
                                "Zorg at bay.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFjYmZmZGQtYzg4YS00ZGE5LTgwYzAtZmQwZjQ2NDliMGVmXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_SY1000_CR0,0,696,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=199EvXTKucc",
                                "PG-13")

too_wong_foo = media.Movie("To Wong Foo: Thanks for Everything, Julie Newmar",
                           "Three drag queens travel cross-country until their "
                           "car breaks down, leaving them stranded in "
                           "a small town.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyNzgxNTk0OF5BMl5BanBnXkFtZTcwOTAzNjgyMQ@@._V1._CR2,3,261,413_.jpg",
                           "https://www.youtube.com/watch?v=N0324KvZc7M",
                           "PG-13")

movies =[ avatar, bird_cage, star_wars, the_matrix, the_fifth_element, too_wong_foo]
fresh_tomatoes.open_movies_page(movies)
""" Call the fresh_tomatoes code to produce the webpage and display it """

