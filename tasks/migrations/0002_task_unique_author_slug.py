# Generated by Django 4.0.4 on 2022-06-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('author', 'slug'), name='unique_author_slug'),
        ),
    ]
