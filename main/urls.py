from django.urls import path
from main import views

urlpatterns = [
    path('', views.home ),
    path('about/', views.about, name='about' ),
    path('about-dev/', views.about_dev, name= 'about-dev'),
    path('news/', views.news, name= 'news'),
    path('weather/', views.weather, name= 'weather'),
    path('search/', views.search, name= 'search'),
    path('savefeedback/', views.savefeedback, name= 'savefeedback'),
    
]