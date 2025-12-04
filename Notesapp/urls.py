from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_newt', views.create_newt, name='create_newt'),
    path('update_newt/<str:pk>', views.update_newt, name='update_newt'),
    path('delete_newt/<str:pk>', views.delete_newt, name='delete_newt'),
    path('toggle_pin/<str:pk>', views.toggle_pin, name='toggle_pin')
]
