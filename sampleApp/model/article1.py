from django.db import models

class article(models.Model):
    title = models.CharField(max_length=200)
    work_text = models.TextField()
    private_text = models.TextField()
    date = models.DateField()
    sleep_duration = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(13)])
    work_system_choices = [
        ('出勤', '出勤'),
        ('出張', '出張'),
        ('テレワーク', 'テレワーク'),
        ('休み', '休み')
    ]
    work_system = models.CharField(max_length=100, choices=work_system_choices)  # 勤務体系
    temperature = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # 気温
    humidity = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)  # 湿度
    expenditure = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(51)])  # 使ったお金
    overall_mood = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(11)])  # 総合的な気分（0から10の10段階）
    overtime_hours = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(25)])  # 残業時間
    save_in_progress = models.BooleanField(default=False)  # フラグを追加

    def __str__(self):
        return self.title

