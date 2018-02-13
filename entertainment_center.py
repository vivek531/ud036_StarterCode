from media import Movie
from fresh_tomatoes import open_movies_page

oceans_8 = Movie(title="OCEAN'S 8",
                 trailer_youtube_url="https://www.youtube.com/watch?v=TTfe2Manwmo",
                 poster_image_url="posters/oceans8.jpeg")

avengers_infinity_war = Movie(title="Avengers Infinity War",
                              trailer_youtube_url="https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                              poster_image_url="posters/avengers_infinity_war.jpeg")

the_space_between_us = Movie(title="The Space Between Us",
                             trailer_youtube_url="https://www.youtube.com/watch?v=sk2mRdxEFuk",
                             poster_image_url="posters/the_space_between_us.jpeg")

beyond = Movie(title="BEYOND",
               trailer_youtube_url="https://www.youtube.com/watch?v=c0gThYUHRTs",
               poster_image_url="posters/beyond.jpeg")

the_rift = Movie(title="The Rift",
                 trailer_youtube_url="https://www.youtube.com/watch?v=TwLVxayxgTw",
                 poster_image_url="posters/the_rift.jpeg")

movies = [oceans_8,
          avengers_infinity_war,
          the_space_between_us,
          beyond,
          the_rift
          ]

if __name__ == "__main__":
    """
    main program to run the application.
    """
    open_movies_page(movies=movies)




