# Generated by Django 3.1.7 on 2021-03-10 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketingTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_tool', models.CharField(choices=[('abc', 'Abc'), ('efg', 'Efg'), ('xyz', 'Xyz')], max_length=10)),
                ('endpoint', models.CharField(max_length=50, null=True)),
                ('authentication_type', models.CharField(choices=[('password', 'Password'), ('token', 'Token')], max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TicketingToolProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.projects')),
                ('ticketing_tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.ticketingtool')),
            ],
        ),
    ]