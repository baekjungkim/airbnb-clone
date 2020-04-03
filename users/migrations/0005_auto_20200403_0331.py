# Generated by Django 2.2.5 on 2020-04-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200403_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
    ]
