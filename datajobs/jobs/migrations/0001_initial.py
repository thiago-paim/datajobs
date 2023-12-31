# Generated by Django 4.2.4 on 2023-09-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("jobkey", models.CharField(blank=True, max_length=50, unique=True)),
                ("url", models.URLField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(blank=True, max_length=100)),
                ("company", models.CharField(blank=True, max_length=100)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("relative_time", models.CharField(blank=True, max_length=50)),
                ("description", models.TextField(blank=True)),
                ("apply_url", models.URLField(blank=True)),
                ("benefits", models.TextField(blank=True)),
                ("html", models.TextField(blank=True)),
            ],
        ),
    ]
