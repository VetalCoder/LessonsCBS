"""
Definition of urls for LessonsCBS.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

    # our routes
    path("lesson-two/", include('lesson_two_routes.urls')),
    path("lesson-two-part2/", include('lesson_two_routes_part2.urls')),
    path("lesson-two-responses/", include('lesson_two_responses.urls', namespace='lesson_two_responses')),
    path("lesson-third/", include('lesson_third_templates.urls')),
    path("lesson-fifth/", include('lesson_fifth_forms.urls')),
    path("lesson-sixth/", include('lesson_sixth_ORM.urls')),
    path("lesson-seventh/", include('lesson_seventh_registration.urls')),
    path("lesson-eighth/", include('lesson_eight_ajax.urls')),
]
