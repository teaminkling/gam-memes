"""Models related to the meme bank."""

from django.db import models
from django.utils.html import format_html


class UserMeme(models.Model):
    """
    A meme that a user has submitted based on a meme template.

    Notes
    -----
    A note to devs: the image is not likely to be viewed by anybody except for the people in a
    game. Keep privacy in mind.

    **Under no circumstances** should any meme URL ever be explicitly mined. Users trust us with
    the memes they make, and we should be mindful of such. As a result, while it might be easier
    to keep URLs small, they are better off as long, unguessable URLs stored on our CDN.
    """

    template = models.ForeignKey(
        to="data_mine.MemeTemplate", null=True, on_delete=models.SET_NULL
    )

    player = models.ForeignKey(
        to="game_state.Player", null=True, on_delete=models.SET_NULL
    )

    url = models.CharField(
        null=True,
        max_length=512,
        unique=True,
        db_index=True,
        verbose_name="URL",
        help_text="The URL to the user meme image stored on our server.",
    )

    game = models.ForeignKey(to="game_state.Game", null=True, on_delete=models.SET_NULL)

    @property
    def image(self: "UserMeme") -> str:
        """
        An embeddable image.

        Returns
        -------
        `str`
            A formatted HTML image.
        """

        style_string: str = (
            "max-height: 256px; filter: drop-shadow(0 0 0.5rem #333333);"
        )

        return format_html(f"<img src='{self.url}' style='{style_string}' />")

    @property
    def thumbnail(self: "UserMeme"):
        """
        An embeddable image for the list display.

        Returns
        -------
        `str`
            A formatted HTML image.
        """

        style_string: str = (
            "max-height: 128px;"
            "width: 100%;"
            "max-width: 128px;"
            "object-fit: cover;"
            "filter: drop-shadow(0 0 0.25rem #333333);"
        )

        return format_html(f"<img src='{self.url}' style='{style_string}' />")

    @property
    def link(self: "UserMeme") -> str:
        """
        A clickable URL for this meme.

        Returns
        -------
        `str`
            A formatted HTML link.
        """

        return format_html(f"<a href='{self.url}' target='_blank'>{self.url}</a>")

    def nuke(self) -> None:
        """
        Remove the URL after making sure the URL's backend has nuked all traces of the image.

        We don't just delete the meme such that the URL is not re-used.
        """

        self.url = None
        self.save()

    def __str__(self):
        return f"UserMeme #{self.id} with URL {self.url} of Template '{self.template}'"

    class Meta:
        verbose_name = "User Meme"

        verbose_name_plural = "User Memes"
