# Generated by Django 3.2.19 on 2023-12-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230619_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bookmarks',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(0, 'Tops'), (1, 'Pants'), (3, 'Accessories'), (3, 'Artwork')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'Out of Stock'), (1, 'In Stock')], default=0),
        ),
    ]