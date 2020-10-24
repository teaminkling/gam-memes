"""Models related to data mining of meme templates."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from meme_bank.models import UserMeme


class MemeTemplate(models.Model):
    """
    A meme template to be used by all game images.

    Notes
    -----
    All images, regardless of source, eventually get stored on our servers.
    """

    url = models.CharField(
        db_index=True,
        max_length=512,
        unique=True,
        verbose_name="URL",
        help_text="The URL to the template image stored on our server.",
    )

    added_timestamp = models.DateTimeField(
        auto_now=True,
        help_text="The timestamp in which the template was data-mined or otherwise added.",
    )

    likes = models.IntegerField(
        default=0,
        help_text="The number of times this template has been liked.",
    )

    dislikes = models.IntegerField(
        default=0,
        help_text="The number of times this template has been disliked.",
    )

    throw_back_probability = models.DecimalField(
        default=0.0,
        decimal_places=4,
        max_digits=16,
        verbose_name="Throw-back Probability",
        help_text=(
            "How likely is it that, when selected, the template will be ignored and a new one "
            "selected? This field is dynamically determined and goes from 0.0 to 1.0."
        ),
        validators=[MaxValueValidator(1.0), MinValueValidator(0.0)],
    )

    staleness_routine_override = models.BooleanField(
        default=False,
        verbose_name="Staleness Routine Override",
        help_text=(
            "If set, the throw-back probability will be frozen and not calculated by the "
            "staleness algorithm."
        ),
    )

    @property
    def use_count(self) -> int:
        """Get the amount of times this template has been used in the game."""

        return UserMeme.objects.filter(template_id=self.id).count()

    use_count.fget.short_description = "Times Used in Memes"

    @property
    def approval_rating(self) -> float:
        """Get the approval heuristic based on view count, likes, and dislikes."""

        # TODO: This is a very basic algorithm for now does not influence view count. Research
        #       must be done to determine a suitable algorithm including view count.

        return float(self.likes - self.dislikes)

    approval_rating.fget.short_description = "Approval Heuristic"

    def __str__(self):
        return f"Meme Template (ID= {self.id}, URL={self.url})"

    class Meta:
        verbose_name = "Meme Template"

        verbose_name_plural = "Meme Templates"
