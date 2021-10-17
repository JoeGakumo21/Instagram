from django.urls import path
from . import views

urlpatterns = [
   path('register/', views.registerPage, name='register'),
   path('login/', views.loginPage, name='login'),
   path('logout/', views.logoutUser, name='logout'),
   path('', views.post, name='post'),
   path('new/', views.create_post, name='postview'),

]