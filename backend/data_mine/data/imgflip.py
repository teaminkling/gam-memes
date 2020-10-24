"""Class dealing with the Imgflip source for meme templates."""

import requests

from requests.models import Response

from backend.data_mine.models import MemeTemplate

IMGFLIP_GET_MEMES_ENDPOINT: str = "https://api.imgflip.com/get_memes"
"""URL for the popular memes endpoint."""


class ImgflipSource:
    """Singleton source containing static methods related to the Imgflip source."""

    @staticmethod
    def populate_popular_memes() -> None:
        """
        Populate the popular memes found from Imgflip.
        """

        response: Response = requests.get(url=IMGFLIP_GET_MEMES_ENDPOINT)

        if not response.ok:
            raise RuntimeError("HTTP problem with popular memes endpoint!")

        popular_memes_json: dict = response.json()

        """
        The GET request sent to Imgflip will return something like this:

        {
            "success": true,
            "data": {
                "memes": [
                    {
                        "id": "61579",
                        "name": "One Does Not Simply",
                        "url": "url_here",
                        "width": 568,
                        "height": 335,
                        "box_count": 2
                    },
                    {
                        "id": "101470",
                        "name": "Ancient Aliens",
                        "url": "url_here",
                        "width": 500,
                        "height": 437,
                        "box_count": 2
                    }
                ]
            }
        }
        """

        if not popular_memes_json.get("success"):
            raise RuntimeError("Upstream problem with popular memes endpoint!")

        # Allow explosion if JSON is malformed/unexpected.

        for template in popular_memes_json["data"]["memes"]:
            # Add unique URLs to the meme templates database.

            url: str = template["url"]

            MemeTemplate.objects.get_or_create(
                url=url,
            )

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
