# Generated by Django 4.1 on 2022-10-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_participant_meetup_slug_speaker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(null=True, upload_to='user_image'),
        ),
    ]
