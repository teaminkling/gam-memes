# Generated by Django 3.1.2 on 2020-10-25 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_mine', '0004_auto_20201025_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memetemplatetogamethrough',
            options={'ordering': ['order']},
        ),
        migrations.RemoveConstraint(
            model_name='memetemplatetogamethrough',
            name='game_template_order_unique',
        ),
    ]
