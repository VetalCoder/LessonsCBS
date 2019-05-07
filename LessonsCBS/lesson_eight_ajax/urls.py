from django.urls import path
from . import views

app_name = 'lesson_eight_ajax'

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('register', views.RegisterFormView.as_view(), name="registration"),
    path("login", views.LoginFormView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),

    path('validate-email/', views.validate_email),
    path('show-three/', views.show_three, name="show_three"),
    path('show-four/', views.show_four, name="show_four"),
    path('add-human/', views.add_human),

    #url(r'^validate-email' , views.validate_email),
    #url(r'^show-three' , views.show_three),
    #url(r'^show-four' , views.show_four),
    #url(r'^add-human/' , views.add_human),
    ]
