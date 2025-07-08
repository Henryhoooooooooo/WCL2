from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('showroom/', views.showroom, name='showroom'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('convai/', views.convai_demo, name='convai_demo'),
    path('assistant/', views.assistant_demo, name='assistant_demo'),
    path('assistant_api/', views.assistant_api, name='assistant_api'),
    path('playcanvas/', views.playcanvas_demo, name='playcanvas_demo'),
]
