from django.urls import path

from . import views

app_name="Distribute"
urlpatterns = [
    path('', views.index, name='index'),
    path('normal/', views.normal, name='normalc'),
    path('vip/', views.vip, name='vipc'),
    path('next/', views.next, name='nextc'),
]