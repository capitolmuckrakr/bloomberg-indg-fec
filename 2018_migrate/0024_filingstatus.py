# Generated by Django 2.0.1 on 2018-04-04 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_2018', '0023_auto_20180314_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilingStatus',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('filing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
