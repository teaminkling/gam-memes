"""Class dealing with the Imgflip source for meme templates."""


class ImgflipSource:
    """Singleton source containing static methods related to the Imgflip source."""

    @staticmethod
    def populate_popular_memes() -> None:
        """Populate the popular memes found from Imgflip."""

        pass

    @staticmethod
    def scrape_user_memes(number: int = 100) -> None:
        """
        Scrape user memes from Imgflip.

        Parameters
        ----------
        number: `int`
            The number of memes to scrape for, at minimum. The function may scrape more than this number.
        """

        raise NotImplementedError("scrape_user_memes is not implemented.")
