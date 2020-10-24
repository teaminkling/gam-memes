# Migration meant to initially populate the MemeTemplate table.

from django.db import migrations

from data_mine.data.imgflip import ImgflipSource


def populate_meme_templates(_0, _1):
    ImgflipSource.populate_popular_memes()


class Migration(migrations.Migration):
    dependencies = [
        ('data_mine', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_meme_templates),
    ]
