from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('weather/', include('weather.urls')),
    path('events/', include('events.urls')),
    path('login/', LoginView.as_view(template_name='users/login.html', success_url='/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
