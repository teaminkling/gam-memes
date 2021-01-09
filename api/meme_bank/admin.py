"""Administrative view objects for meme bank models."""

from django.contrib import admin

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
