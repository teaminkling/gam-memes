"""Administrative view objects for data mine models."""

from django.contrib import admin
from django.utils.html import format_html

from data_mine.models import MemeTemplate


@admin.register(MemeTemplate)
class MemeTemplateAdmin(admin.ModelAdmin):
    """Admin view for the `MemeTemplate` model."""

    fields = (
        "image",
        "url",
        "link",
        "likes",
        "dislikes",
        "approval_rating",
        "use_count",
        "throw_back_probability",
    )

    list_display = (
        "id",
        "thumbnail",
        "link",
        "likes",
        "dislikes",
        "approval_rating",
        "use_count",
        "throw_back_probability",
    )

    readonly_fields = (
        "image",
        "link",
        "use_count",
        "approval_rating",
    )

    @staticmethod
    def image(instance: MemeTemplate) -> str:
        """
        An embeddable image.

        Parameters
        ----------
        instance : `MemeTemplate`
            The template under examination.

        Returns
        -------
        `str`
            A formatted HTML image.
        """

        style_string: str = "max-height: 256px; filter: drop-shadow(0 0 0.5rem #333333);"

        return format_html(f"<img src='{instance.url}' style='{style_string}' />")

    @staticmethod
    def thumbnail(instance: MemeTemplate):
        """
        An embeddable image for the list display.

        Parameters
        ----------
        instance : `MemeTemplate`
            The meme under examination.

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

        return format_html(f"<img src='{instance.url}' style='{style_string}' />")

    @staticmethod
    def link(instance: MemeTemplate) -> str:
        """
        A clickable URL for this meme.

        Parameters
        ----------
        instance : `MemeTemplate`
            The template under examination.

        Returns
        -------
        `str`
            A formatted HTML link.
        """

        return format_html(f"<a href='{instance.url}' target='_blank'>{instance.url}</a>")
