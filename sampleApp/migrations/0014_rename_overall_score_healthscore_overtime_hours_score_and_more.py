# Generated by Django 5.0.3 on 2024-06-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApp', '0013_rename_text_article_private_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthscore',
            old_name='overall_score',
            new_name='overtime_hours_score',
        ),
        migrations.AddField(
            model_name='healthscore',
            name='sentiment_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthscore',
            name='total_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
