# Generated by Django 4.0 on 2022-02-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
            ],
        ),
    ]
