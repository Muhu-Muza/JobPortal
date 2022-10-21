# Generated by Django 4.0.6 on 2022-10-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_company_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='nature',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part TIme'), ('N/A', 'N/A'), ('Internship', 'INTERNSHIP')], default='N/A', max_length=100),
        ),
    ]
