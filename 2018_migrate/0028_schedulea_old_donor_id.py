# Generated by Django 2.0.1 on 2018-07-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_2018', '0027_auto_20180721_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulea',
            name='old_donor_id',
            field=models.CharField(blank=True, help_text='terrible hack for editing donor totals, do not manually edit!', max_length=255, null=True),
        ),
    ]
