# Generated by Django 4.1.3 on 2023-03-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0002_alter_curriculumvita_end_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="description",
            field=models.TextField(default="To Do"),
        ),
    ]
