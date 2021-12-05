from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="home"),
    path('graphs/', views.graphs, name="graphs"),
    # path('auth/signin/', views.signin, name='auth'),
]