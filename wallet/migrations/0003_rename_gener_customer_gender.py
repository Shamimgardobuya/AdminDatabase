# Generated by Django 4.0.6 on 2022-07-26 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_customer_nationality_customer_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='gener',
            new_name='gender',
        ),
    ]