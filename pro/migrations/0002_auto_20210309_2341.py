# Generated by Django 3.1.7 on 2021-03-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketingtool',
            name='password',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticketingtool',
            name='token',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticketingtool',
            name='username',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
