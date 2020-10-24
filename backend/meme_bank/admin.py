"""Administrative view objects for meme bank models."""

from django.contrib import admin
from django.utils.html import format_html

from meme_bank.models import UserMeme


@admin.register(UserMeme)
class UserMemeAdmin(admin.ModelAdmin):
    fields = (
        "image",
        "url",
        "link",
        "template",
        "player",
    )

    list_display = (
        "id",
        "thumbnail",
        "link",
        "template",
        "player",
    )

    readonly_fields = (
        "image",
        "link",
    )

    @staticmethod
    def image(instance: UserMeme) -> str:
        """
        An embeddable image.

        Parameters
        ----------
        instance : `UserMeme`
            The template under examination.

        Returns
        -------
        `str`
            A formatted HTML image.
        """

        style_string: str = "max-height: 256px; filter: drop-shadow(0 0 0.5rem #333333);"

        return format_html(f"<img src='{instance.url}' style='{style_string}' />")

    @staticmethod
    def thumbnail(instance: UserMeme):
        """
        An embeddable image for the list display.

        Parameters
        ----------
        instance : `UserMeme`
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
    def link(instance: UserMeme) -> str:
        """
        A clickable URL for this meme.

        Parameters
        ----------
        instance : `UserMeme`
            The template under examination.

        Returns
        -------
        `str`
            A formatted HTML link.
        """

        return format_html(f"<a href='{instance.url}' target='_blank'>{instance.url}</a>")
