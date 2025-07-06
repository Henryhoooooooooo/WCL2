
from django.shortcuts import render


def index(request):
    return render(request, 'exhibition/main.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def showroom(request):
    return render(request, 'exhibition/index.html')

# 用戶註冊視圖
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
