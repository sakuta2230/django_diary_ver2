from django.shortcuts import render, get_object_or_404
from sampleApp.model import article1
from sampleApp.model import health_score

def detail(request, article_id):
    # 記事の取得
    article_instance = get_object_or_404(article1.article, pk=article_id)

    # 記事に対応するヘルススコアの取得（存在しない場合もあるため、存在しない場合は None にする）
    healthscore = health_score.HealthScore.objects.filter(article_id=article_id).first()

    # コンテキストに記事とヘルススコアを追加
    context = {
        'object': article_instance,
        'health_score': healthscore,
    }

    return render(request, 'detail.html', context)