# Generated by Django 3.2.6 on 2021-09-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='height',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='examinerprofile',
            name='height',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
