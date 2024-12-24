from django.urls import path
from . import  views


app_name = 'videos'

urlpatterns = [
    path('list/', views.video_list, name='list'),
    path('create/', views.video_create, name='create'),
    path('detail/<int:pk>/', views.video_detail, name='detail'),
    path('update/<int:pk>/', views.video_update, name='update'),
    path('delete/<int:pk>/', views.video_delete, name='delete'),
]
