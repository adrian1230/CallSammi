# Generated by Django 3.0.4 on 2020-03-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('understand', '0002_auto_20200308_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='category',
            field=models.CharField(blank=True, choices=[('healthcare', 'healthcare'), ('technology', 'technology'), ('science', 'science'), ('beauty', 'beauty'), ('entertainment', 'entertainment'), ('politic', 'politic'), ('culinary', 'culinary'), ('others', 'others')], default='NA', max_length=70),
        ),
        migrations.AlterField(
            model_name='result',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
