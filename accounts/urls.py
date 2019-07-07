from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index, logout_view

# app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('password_reset/', index, name='password_reset'),
    path('logout/', logout_view, name='logout'),
    path('index/', index, name='accounts.index'),
]
