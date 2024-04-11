from django.urls import path
from centre import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
]