# Generated by Django 3.2.9 on 2021-11-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20211107_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isUpdated',
            field=models.BooleanField(default=False),
        ),
    ]
