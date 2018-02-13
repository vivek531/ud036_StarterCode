class Movie(object):
    """
    class for making movies.
    """

    def __init__(self, title, trailer_youtube_url, poster_image_url):
        """

        :param title: title of the movie
        :param trailer_youtube_url: youtube url for the trailer
        :param poster_image_url: poster of the movie
        """

        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

