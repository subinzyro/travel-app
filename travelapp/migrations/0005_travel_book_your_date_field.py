# Generated by Django 5.0.1 on 2024-03-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_alter_travel_book_num_travelers'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel_book',
            name='your_date_field',
            field=models.DateField(null=True),
        ),
    ]
