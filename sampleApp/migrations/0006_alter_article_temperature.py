# Generated by Django 5.0.3 on 2024-05-08 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApp', '0005_rename_sleep_duration_hours_article_sleep_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
