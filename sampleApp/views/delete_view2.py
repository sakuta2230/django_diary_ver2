from django.shortcuts import render, get_object_or_404, redirect
from sampleApp.model import article1

#変更
def delete_article(request, article_id):
    article_instance = get_object_or_404(article1.article, pk=article_id)

    if request.method == 'POST':
        article_instance.delete()
        return redirect('list')

    return render(request, 'confirm_delete.html', {'object': article_instance})