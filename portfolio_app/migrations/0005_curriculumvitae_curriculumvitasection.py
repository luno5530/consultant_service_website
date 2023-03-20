# Generated by Django 4.1.3 on 2023-03-20 13:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0004_remove_curriculumvitasection_origin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CurriculumVitae",
            fields=[
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="portfolio_app.profile",
                    ),
                ),
                (
                    "starting_date",
                    models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
                ),
                ("end_date", models.DateField(default="2023-03-20")),
            ],
        ),
        migrations.CreateModel(
            name="CurriculumVitaSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=255)),
                (
                    "starting_date",
                    models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
                ),
                ("end_date", models.DateField(default="2023-03-20")),
                ("content", models.TextField(max_length=255)),
                (
                    "origin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portfolio_app.curriculumvitae",
                    ),
                ),
            ],
        ),
    ]
