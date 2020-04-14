# Generated by Django 2.2.5 on 2020-04-14 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20200414_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to='reservations.Status'),
        ),
    ]
