# Generated by Django 3.0.4 on 2020-03-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('understand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='summarized_text',
            field=models.TextField(),
        ),
    ]
