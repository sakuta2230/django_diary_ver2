from django.contrib.auth import logout
from django.shortcuts import redirect
##変更
def logoutfunc(request):
    logout(request)
    return redirect('login')