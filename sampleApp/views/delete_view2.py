from django.shortcuts import render, get_object_or_404, redirect
from sampleApp.model import article1
import logging
#変更

diary_logger = logging.getLogger('diary')#ロガー取得

def delete_article(request, article_id):
    article_instance = get_object_or_404(article1.article, pk=article_id)

    if request.method == 'POST':
        diary_logger.info(f"Diary entry deleted: {article_instance.title}")#ロガーに記入。消す前にタイトルを取得して出力
        article_instance.delete()
        return redirect('list')

    return render(request, 'confirm_delete2.html', {'object': article_instance})