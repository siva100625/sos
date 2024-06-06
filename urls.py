from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('share-location/', views.share_location, name='share_location'),
    path('', views.home, name='home'),
]
