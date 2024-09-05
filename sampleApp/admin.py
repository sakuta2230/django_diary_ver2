# sampleApp/admin.py
from django.contrib import admin
from sampleApp.model.article1 import article
from sampleApp.model.health_score import HealthScore
 # モデルのインポート

admin.site.register(article)  # article1モデルを管理画面に登録
admin.site.register(HealthScore)  # health_scoreモデルを管理画面に登録
