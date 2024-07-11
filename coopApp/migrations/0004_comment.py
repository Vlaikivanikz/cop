# Generated by Django 5.0.6 on 2024-07-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coopApp', '0003_alter_portfolio_ifonlinework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('ref', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=50)),
                ('verified', models.CharField(max_length=10)),
            ],
        ),
    ]
