# Generated by Django 4.2.5 on 2024-12-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academics", "0002_auto_20211223_1902"),
    ]

    operations = [
        migrations.AlterField(
            model_name="icsr",
            name="course_name",
            field=models.TextField(default="", max_length=500),
        ),
    ]