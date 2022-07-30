# Generated by Django 4.0.6 on 2022-07-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]