# Generated by Django 4.0.6 on 2022-07-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ryaba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oformlenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('city', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('choice', models.CharField(choices=[('Перезвонить мне', 'Перезвонить мне'), ('Не звонить мне', 'Не звонить мне')], max_length=20)),
                ('opisanie', models.TextField(max_length=200)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
