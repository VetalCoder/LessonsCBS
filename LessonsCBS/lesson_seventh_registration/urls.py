from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainView.as_view()),
    path("logout", views.LogoutView.as_view()),
    path("login", views.LoginFormView.as_view()),
    path("registration", views.RegisterFormView.as_view()),

    # advansed registration
    #path("registration", views.AdvansedRegisterFormView.as_view()),
]
