# Generated by Django 2.0.1 on 2018-02-16 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_2018', '0007_scheduleb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('form_type', models.CharField(blank=True, max_length=255, null=True)),
                ('filer_committee_id_number', models.CharField(blank=True, max_length=255, null=True)),
                ('filing_id', models.IntegerField(blank=True, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('back_reference_tran_id_number', models.CharField(blank=True, max_length=255, null=True)),
                ('back_reference_sched_name', models.CharField(blank=True, max_length=255, null=True)),
                ('entity_type', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_organization_name', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_street_1', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_street_2', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_city', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_state', models.CharField(blank=True, max_length=30, null=True)),
                ('payee_zip', models.CharField(blank=True, max_length=10, null=True)),
                ('election_code', models.CharField(blank=True, max_length=255, null=True)),
                ('election_other_description', models.CharField(blank=True, max_length=255, null=True)),
                ('dissemination_date', models.CharField(blank=True, max_length=255, null=True)),
                ('expenditure_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('expenditure_date', models.CharField(blank=True, max_length=255, null=True)),
                ('calendar_y_t_d_per_election_office', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('expenditure_purpose_descrip', models.CharField(blank=True, max_length=255, null=True)),
                ('category_code', models.CharField(blank=True, max_length=255, null=True)),
                ('payee_cmtte_fec_id_number', models.CharField(blank=True, max_length=255, null=True)),
                ('support_oppose_code', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_id_number', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_office', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_district', models.CharField(blank=True, max_length=255, null=True)),
                ('candidate_state', models.CharField(blank=True, max_length=255, null=True)),
                ('completing_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('completing_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('completing_middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('completing_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('completing_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('date_signed', models.CharField(blank=True, max_length=255, null=True)),
                ('memo_code', models.CharField(blank=True, max_length=255, null=True)),
                ('memo_text_description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
