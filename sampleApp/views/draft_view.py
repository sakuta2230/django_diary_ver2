from django.shortcuts import render
from sampleApp.model import article1

def draft_articles_view(request):
    # 保存中のフラグがTrueの下書き記事を取得
    draft_articles = article1.article.objects.filter(save_in_progress=True)
    
    return render(request, 'draft_list.html', {'draft_articles': draft_articles})