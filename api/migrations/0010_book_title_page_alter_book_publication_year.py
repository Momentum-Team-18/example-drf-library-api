# Generated by Django 4.1.3 on 2023-06-28 00:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_user_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="title_page",
            field=models.ImageField(blank=True, null=True, upload_to="title_pages"),
        ),
        migrations.AlterField(
            model_name="book",
            name="publication_year",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(300),
                    django.core.validators.MaxValueValidator(2023),
                ],
            ),
        ),
    ]
