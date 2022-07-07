from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/',
         LoginView.as_view(
            template_name='login.html',
            extra_context={'button': 'Войти', 'header': 'Войти в систему'},
            next_page='index'),
         name='login'),
    path('logout/',
         LogoutView.as_view(
            template_name='login.html',
            extra_context={'button': 'Выйти', 'header': 'Выйти из системы'},
            next_page='login'),
         name='logout'),
    path('add_host/', views.add_host, name='add_host'),
    path('hosts/<int:host_id>/edit_host/', views.edit_host, name='edit_host' )
]
