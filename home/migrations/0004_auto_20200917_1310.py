# Generated by Django 3.1.1 on 2020-09-17 13:10

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200917_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calorie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='fats',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='proteins',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='detail',
            name='active',
            field=models.CharField(choices=[('High', 'High'), ('Mid', 'Mid'), ('Low', 'Low')], default=home.models.activity['Low'], max_length=7),
        ),
    ]
