# Generated by Django 5.0.3 on 2024-06-05 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_followers_likepost_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Followers',
        ),
        migrations.DeleteModel(
            name='LikePost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
