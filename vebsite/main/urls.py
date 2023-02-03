from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('information/', views.information, name='information'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('del/<str:id>', views.delete_task, name='delete'),
]
