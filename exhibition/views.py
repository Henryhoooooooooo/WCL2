# PlayCanvas 虛擬展廳頁面
def playcanvas_demo(request):
    return render(request, 'exhibition/playcanvas.html')
# AI數字人助理頁面
def assistant_demo(request):
    return render(request, 'exhibition/assistant.html')
# AI 數字人助理 API（簡單範例，回應庫存/商品等）
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def assistant_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg = data.get('message', '').lower()
        # 這裡可根據 msg 查詢資料庫，這裡僅做範例
        if '庫存' in msg or 'stock' in msg:
            # 假設查詢商品庫存
            # 例如：Product.objects.get(name='xxx').stock
            reply = '目前A商品庫存：42 件。'  # 這裡可換成真實查詢
        elif '商品' in msg or 'product' in msg:
            reply = '我們有A、B、C三款時尚新品，歡迎選購！'
        else:
            reply = '您好，我是AI數字人，可以查詢商品、庫存、訂單等，請問有什麼可以幫您？'
        return JsonResponse({'reply': reply})
    return JsonResponse({'reply': '僅支援POST請求'})

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

# Convai Web Demo 頁面
def convai_demo(request):
    return render(request, 'exhibition/convai.html')
