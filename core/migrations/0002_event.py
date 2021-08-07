# Generated by Django 3.2.6 on 2021-08-07 18:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('type', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('user', models.ManyToManyField(related_name='volunteer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
