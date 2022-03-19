from django.urls import path
# Я правильно понял, что в импортах проблемой было то, что их нужно 
# было разделить на группы?
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.groups_list),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
