from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.loginPage, name='login'),
    # path('password_reset', views.password_reset_request, name="password_reset")
    path('reset_password/',views.reset_password,name='reset_password'),
    path('reset_password/<str:id>',views.create_password,name='create_password'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('Fporegistation/',views.Fporegistation,name='Fporegistation'),
    path('fpoverify/<str:id>',views.Fpoverify,name='Fpoverify'),
]
