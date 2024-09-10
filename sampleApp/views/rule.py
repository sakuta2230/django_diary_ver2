from django.shortcuts import render

def rule_view(request):
    return render(request, 'rule.html')
