from django.shortcuts import render
from sampleApp.model import article1
from sampleApp.model import health_score
from django.contrib.auth.decorators import login_required

@ login_required
def list(request):
    published_articles = article1.article.objects.filter(save_in_progress=False)
    draft_articles = article1.article.objects.filter(save_in_progress=True)
    healthscore=health_score.HealthScore.objects.all
    context = {
        'published_articles': published_articles,
        'draft_articles': draft_articles,
        'healthscore':healthscore
    }
    return render(request,'list3.html',context)