"""Models related to the meme bank."""

from django.db import models


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

    If we ever implement an image deletion mechanism, this will not be the app's responsibility.
    The URL will simply be nulled.
    """

    template = models.ForeignKey(to="data_mine.MemeTemplate", null=True, on_delete=models.SET_NULL)

    player = models.ForeignKey(to="game_state.Player", null=True, on_delete=models.SET_NULL)

    url = models.CharField(
        null=True,
        max_length=512,
        unique=True,
        db_index=True,
        verbose_name="URL",
        help_text="The URL to the user meme image stored on our server.",
    )

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
