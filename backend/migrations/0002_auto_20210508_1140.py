# Generated by Django 3.2.2 on 2021-05-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]