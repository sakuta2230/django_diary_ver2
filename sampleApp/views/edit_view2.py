from django.shortcuts import redirect, render, get_object_or_404
from sampleApp.model.article1 import article

def edit(request, article_id):
    article_instance = get_object_or_404(article, pk=article_id)
    if request.method == 'POST':
        adtitle = request.POST.get('title')
        work_text = request.POST.get('work_text')
        private_text = request.POST.get('private_text')
        addate = request.POST.get('date')
        adsleep_duration = float(request.POST.get('sleep_duration'))
        adwork_system = request.POST.get('work_system')
        adexpenditure = float(request.POST.get('expenditure'))
        adoverall_mood = float(request.POST.get('overall_mood'))
        
        save_in_progress = 'save_in_progress' in request.POST

        article_instance.title = adtitle
        article_instance.work_text = work_text
        article_instance.private_text = private_text
        article_instance.date = addate
        article_instance.sleep_duration = adsleep_duration
        article_instance.work_system = adwork_system
        article_instance.expenditure = adexpenditure
        article_instance.overall_mood = adoverall_mood
        article_instance.save_in_progress = save_in_progress
        # Debug prints before saving
        print(f"Before save: article_instance.save_in_progress = {article_instance.save_in_progress}")
        article_instance.save()
        # Debug prints after saving
        print(f"After save: save_in_progress = {save_in_progress}")
        print(f"After save: article_instance.save_in_progress = {article_instance.save_in_progress}")
        return redirect('list')
    else:
        return render(request, 'edit.html', {'object': article_instance})