# Generated by Django 3.2.6 on 2021-08-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210811_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='id',
        ),
        migrations.RemoveField(
            model_name='document',
            name='id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.RemoveField(
            model_name='statusbar',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.RemoveField(
            model_name='volunteerslot',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='note_id',
            field=models.CharField(default="don't render this field, it's just for the id number", max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='alert',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statusbar',
            name='unfinished',
            field=models.BooleanField(default=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='volunteerslot',
            name='text_slot',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
