from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('qwerty', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.delete, name='delete'),
    path('<int:pk>/detels/', views.detels, name='detels'),
]
