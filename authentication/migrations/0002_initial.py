# Generated by Django 4.1 on 2023-10-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='books',
            field=models.ManyToManyField(related_name='users', to='book.book'),
        ),
    ]
