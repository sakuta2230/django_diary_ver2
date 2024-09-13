from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # 追加
@login_required

def rule_view(request):
    return render(request, 'rule.html')
