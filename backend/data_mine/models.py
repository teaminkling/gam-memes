"""Models related to data mining of meme templates."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html

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

    likes = models.PositiveIntegerField(
        default=0,
        help_text="The number of times this template has been liked.",
    )

    dislikes = models.PositiveIntegerField(
        default=0,
        help_text="The number of times this template has been disliked.",
    )

    throw_back_probability = models.DecimalField(
        default=0.0,
        decimal_places=4,
        max_digits=16,
        verbose_name="Throw-back Probability",
        validators=[MaxValueValidator(1.0), MinValueValidator(0.0)],
        help_text=(
            "How likely is it that, when selected, the template will be ignored and a new one "
            "selected? This field is dynamically determined and goes from 0.0 to 1.0."
        ),
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

    @property
    def image(self: "MemeTemplate") -> str:
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
    def thumbnail(self: "MemeTemplate"):
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
    def link(self: "MemeTemplate") -> str:
        """
        A clickable URL for this meme.

        Returns
        -------
        `str`
            A formatted HTML link.
        """

        return format_html(f"<a href='{self.url}' target='_blank'>{self.url}</a>")

    def __str__(self):
        return f"Meme Template #{self.id} (URL={self.url})"

    class Meta:
        verbose_name = "Meme Template"

        verbose_name_plural = "Meme Templates"


class MemeTemplateToGameThrough(models.Model):
    """Through model for `MemeTemplate`s in a `Game`."""

    template = models.ForeignKey(to="data_mine.MemeTemplate", on_delete=models.CASCADE)

    game = models.ForeignKey(to="game_state.Game", on_delete=models.CASCADE)

    order = models.PositiveSmallIntegerField(
        help_text=(
            "The order-by field per-game. You can have the same ordering value for memes but this "
            "may have unpredictable results. This field is automatically set to N+1 if left as 0."
        )
    )

    def save(self, **kwargs):
        # Ensure order is +1 of what currently exists if creating a new order.

        if not self.pk or not self.order:
            template_count: int = MemeTemplateToGameThrough.objects.filter(
                game__room_key=self.game.room_key,
            ).count()

            self.order = template_count + 1

        # The game can be created in the same step. Ensure it is saved.

        return super().save(**kwargs)

    class Meta:
        ordering = ["order"]

        constraints = (
            models.constraints.UniqueConstraint(
                name="no_duplicate_templates_for_a_game",
                fields=("game", "template"),
            ),
        )
