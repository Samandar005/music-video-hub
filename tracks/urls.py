from django.urls import path
from . import  views


app_name = 'tracks'

urlpatterns = [
    path('list/', views.track_list, name='list'),
    path('create/', views.track_create, name='create'),
    path('detail/<int:pk>/', views.track_detail, name='detail'),
    path('update/<int:pk>/', views.track_update, name='update'),
    path('delete/<int:pk>/', views.track_delete, name='delete'),
]
