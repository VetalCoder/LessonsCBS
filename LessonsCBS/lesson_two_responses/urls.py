from django.urls import path, re_path, include
from . import views

app_name = "lesson_two_responses"

urlpatterns = [
    path("", views.hello_response),                                 # http://localhost:8000/lesson-two-responses/
    path('redirect/', views.http_redirect),                         # http://localhost:8000/lesson-two-responses/redirect/
    path('name-redirect/', views.http_name_redirect),               # http://localhost:8000/lesson-two-responses/name-redirect/
    path('fun/', views.fun, name="fun"),                            # http://localhost:8000/lesson-two-responses/fun/
    path('render-html/', views.render_html),                        # http://localhost:8000/lesson-two-responses/render-html/  
    path('render-template/', views.render_template),                # http://localhost:8000/lesson-two-responses/render-template/
    path('render-template/form-handler/', views.form_handler),      # http://localhost:8000/lesson-two-responses/render-template/form-handler/
]

