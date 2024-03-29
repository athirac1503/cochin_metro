# Generated by Django 3.2.13 on 2022-06-08 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_signup',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('contact_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metro.userregistration')),
            ],
            options={
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='BookTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=20)),
                ('ticket_from', models.CharField(max_length=40)),
                ('ticket_to', models.CharField(max_length=40)),
                ('no_passenger', models.BigIntegerField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='metro.userregistration')),
            ],
            options={
                'db_table': 'ticket_book',
            },
        ),
    ]
