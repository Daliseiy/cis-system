# Generated by Django 2.2.6 on 2020-05-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisdb', '0003_auto_20200513_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='university_education',
            field=models.CharField(default='None', help_text='University of Technology, Nigeria - (2019-2024)', max_length=250),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='genotype',
            field=models.CharField(blank=True, choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('Other', 'Others: CC, AC..')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=15),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7),
        ),
    ]
