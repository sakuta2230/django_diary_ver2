# sampleApp/admin.py
from django.contrib import admin
from .models import article1, health_score  # モデルのインポート

admin.site.register(article1)  # article1モデルを管理画面に登録
admin.site.register(health_score)  # health_scoreモデルを管理画面に登録
