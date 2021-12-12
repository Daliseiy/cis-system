# Generated by Django 2.2.6 on 2020-05-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisdb', '0007_auto_20200515_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='allergies',
            field=models.CharField(default='No Allegries', max_length=1000),
        ),
        migrations.AddField(
            model_name='citizen',
            name='name_of_children',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='citizen',
            name='number_of_children',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='disability',
            field=models.CharField(default='No Disablilites', help_text='Specify disability and cause and time of disablity \n e.g Blindess-Car Accident 2012', max_length=1000),
        ),
    ]