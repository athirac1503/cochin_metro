# Generated by Django 3.2.13 on 2022-06-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0002_contact_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookticket',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bookticket',
            name='time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]