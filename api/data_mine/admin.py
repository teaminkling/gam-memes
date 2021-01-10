"""Administrative view objects for data mine models."""

from django.contrib import admin

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
