# Generated by Django 4.2.11 on 2024-03-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='giorgi', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='utsunashvili', max_length=200),
            preserve_default=False,
        ),
    ]