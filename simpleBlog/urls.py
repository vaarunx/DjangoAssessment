
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/" ,views.register , name = "register" ),
    path("login/" ,auth_views.LoginView.as_view(template_name = 'blog/login.html') , name = "login" ),
    path("logout/" ,auth_views.LogoutView.as_view(template_name = 'blog/logout.html') , name = "logout" ),
    path("" ,views.dashboard, name = "dashboard" ),



]
