from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('logged/', views.loggedPage, name='login_home'),
    path('logout/', views.logoutUser, name='logout'),
    path('cadastro/', views.cadastroPage, name='cadastro'),
]