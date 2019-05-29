# Generated by Django 2.2 on 2019-05-09 02:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0014_auto_20190509_0249'),
        ('production', '0002_profile_of_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile_of_Actor',
            new_name='ProfileOfActor',
        ),
        migrations.RenameModel(
            old_name='Profile_of_Director',
            new_name='ProfileOfDirector',
        ),
        migrations.RenameModel(
            old_name='Profile_of_Production',
            new_name='ProfileOfProduction',
        ),
        migrations.RenameModel(
            old_name='Profile_of_User',
            new_name='ProfileOfUser',
        ),
    ]
