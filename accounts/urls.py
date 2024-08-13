from django.urls import path ,include
from .views import *

app_name ='accounts'
urlpatterns = [
    path("",login_view,name='login'),
    path("login/",login_view,name='user_login'),
    path("logout/",logout_view,name='logout'),
    
    path("about/",about_view,name='about'),
    path("register/",register_view,name='register'),
    path("profile/",profile,name='profile'),
    
    
]
