from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

#更新
def signupfunc(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'パスワードが一致しません。'})
        
        if len(password1) < 8 or not any(c.isalpha() for c in password1) or not any(c.isdigit() for c in password1):
            return render(request, 'signup.html', {'error': 'パスワードは8文字以上で、少なくとも1つの数字と1つの文字を含む必要があります。'})
        
        try:
            User.objects.create_user(username, '', password1)
            return render(request, 'signup.html', {'success': 'ユーザー登録が完了しました。'})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザー名はすでに使用されています。'})
    
    return render(request, 'signup.html',{'signinuser':'サインインしてください'})