# Generated by Django 5.1.6 on 2025-03-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
