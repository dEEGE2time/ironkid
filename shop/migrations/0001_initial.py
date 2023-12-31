# Generated by Django 4.2.8 on 2023-12-25 18:10

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=80, unique=True)),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=80, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("XS", "XS"),
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("XL", "XL"),
                            ("XXL", "XXL"),
                        ],
                        default=0,
                        max_length=3,
                    ),
                ),
                ("price", models.FloatField()),
                ("description", models.TextField()),
                (
                    "featured_image",
                    cloudinary.models.CloudinaryField(
                        default="placeholder", max_length=255, verbose_name="image"
                    ),
                ),
                ("image_alt", models.CharField(default="alt", max_length=100)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Out of Stock"), (1, "In Stock")], default=0
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
