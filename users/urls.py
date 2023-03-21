from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='password_change_done'),
]
