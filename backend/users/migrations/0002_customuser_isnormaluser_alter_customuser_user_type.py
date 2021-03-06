# Generated by Django 4.0.5 on 2022-07-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isNormalUser',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'superadmin'), (2, 'admin'), (3, 'normaluser')], null=True),
        ),
    ]
