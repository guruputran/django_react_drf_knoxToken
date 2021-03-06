# Generated by Django 4.0.5 on 2022-07-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_isadminuser_customuser_issuperuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'superadmin'), (2, 'admin'), (3, 'normaluser')], default='normaluser', null=True),
        ),
    ]
