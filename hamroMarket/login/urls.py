from django.urls import path
from . import views, forms
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('auth/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('redirect/', views.template_loader),
    # path('', views.template_loader),
    path('register/', views.signup, name = 'user_register'),
    # path('register/', views.signup, name='registerId')
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout')

]