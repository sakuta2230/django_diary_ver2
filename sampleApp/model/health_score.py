from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .article1 import article
from sampleApp.views.weather_view import calculate_health_score
from afinn import Afinn

class HealthScore(models.Model):
    article = models.OneToOneField(article, on_delete=models.CASCADE, related_name='health_score')
    work_text_score = models.FloatField(null=True, blank=True)
    private_text_score = models.FloatField(null=True, blank=True)
    weather_score = models.FloatField(null=True, blank=True)
    work_system_score = models.FloatField(null=True, blank=True)
    expenditure_score = models.FloatField(null=True, blank=True)
    overall_mood_score = models.FloatField(null=True, blank=True)
    sleep_duration_score = models.FloatField(null=True, blank=True)
    overtime_hours_score = models.FloatField(null=True, blank=True)
    total_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"HealthScore for {self.article.title}"

def calculate_and_save_health_score(article_instance):
    temperature = float(article_instance.temperature) if article_instance.temperature is not None else 0.0
    humidity = float(article_instance.humidity) if article_instance.humidity is not None else 0.0

    afinn = Afinn()
    work_text_score = min(float(afinn.score(article_instance.work_text) * 2), 10)  # 0から10の範囲に制限
    private_text_score = min(float(afinn.score(article_instance.private_text) * 2), 10)  # 0から10の範囲に制限

    weather_score = min(float(calculate_health_score(temperature, humidity)) / 10, 10)  # 0から10の範囲に制限

    work_system_scores = {'出勤': 3, '出張': 1, 'テレワーク': 5, '休み': 10}
    work_system_score = float(work_system_scores.get(article_instance.work_system, 0))

    expenditure_score = min(float(article_instance.expenditure) * 0.2, 10)  # 0から10の範囲に制限

    overall_mood_score = min(float(article_instance.overall_mood) * 1, 10)  # 0から10の範囲に制限

    sleep_duration_score = min(float(article_instance.sleep_duration) * 0.83, 10)  # 0から10の範囲に制限

    overtime_hours_score = min(float(article_instance.overtime_hours) * 0.4, 10)  # 0から10の範囲に制限

    total_score = round(
    work_text_score + private_text_score + weather_score + work_system_score +
    expenditure_score + sleep_duration_score + overtime_hours_score, 1
    )


    health_score_instance, created = HealthScore.objects.get_or_create(
        article=article_instance,
        defaults={
            'work_text_score': work_text_score,
            'private_text_score': private_text_score,
            'weather_score': weather_score,
            'work_system_score': work_system_score,
            'expenditure_score': expenditure_score,
            'overall_mood_score': overall_mood_score,
            'sleep_duration_score': sleep_duration_score,
            'overtime_hours_score': overtime_hours_score,
            'total_score': total_score
        }
    )

    if not created:
        health_score_instance.work_text_score = work_text_score
        health_score_instance.private_text_score = private_text_score
        health_score_instance.weather_score = weather_score
        health_score_instance.work_system_score = work_system_score
        health_score_instance.expenditure_score = expenditure_score
        health_score_instance.overall_mood_score = overall_mood_score
        health_score_instance.sleep_duration_score = sleep_duration_score
        health_score_instance.overtime_hours_score = overtime_hours_score
        health_score_instance.total_score = total_score
        health_score_instance.save()

@receiver(post_save, sender=article)
def post_save_article(sender, instance, created, **kwargs):
    calculate_and_save_health_score(instance)

