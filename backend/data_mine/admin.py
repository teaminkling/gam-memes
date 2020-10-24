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
    def image(instance) -> str:
        """

        Parameters
        ----------
        instance :

        Returns
        -------

        """

        return format_html(f"<img src='{instance.url}' style='max-height: 256px' />")

    @staticmethod
    def link(instance) -> str:
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
