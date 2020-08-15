from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MemeTemplate(models.Model):
    """
    A meme template to be used by all game images.

    Notes
    -----
    All images, regardless of source, eventually get stored on our servers.
    """

    url = models.CharField(
        db_index=True,
        max_lengh=512,
        unique=True,
        help_text="The URL to the template image stored on our server.",
    )

    added_timesteamp = models.DateTimeField(
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
        help_text=(
            "How likely is it that, when selected, the meme template will simply be ignored and a new one selected? "
            "The default value is 0.0 (0%). This field is dynamically determined,"
        ),
        validators=[
            MaxValueValidator(1.0), MinValueValidator(0.0),
        ],
    )

    staleness_routine_override = models.DateTimeField(
        null=True,
        blank=True,
        help_text=(
            "If set to the date in which the override was last added, the throw_back_probability will be frozen and "
            "not calculated by the staleness algorithm."
        ),
    )

    @property
    def use_count(self):
        """Get the amount of times this template has been used in the game."""

        raise NotImplemented("use_count has not been implemented.")

    @property
    def approval_rating(self):
        """Get the approval heuristic based on view count, likes, and dislikes."""

        raise NotImplemented("approval_rating has not been implemented.")
