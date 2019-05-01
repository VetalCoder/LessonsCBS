from django.urls import path
from . import views


urlpatterns = [
    path("test-view", views.test_view),             # http://localhost:8000/lesson-fifth/test-view

    # html form
    path("html-form", views.show_html_form),        # http://localhost:8000/lesson-fifth/html-form
    path("file-input/", views.file_input),
    path("search/", views.search),

    # models form
    path("", views.show_model_form),                # http://localhost:8000/lesson-fifth/
    path("add-article/", views.add_article),
    path("add-author/", views.add_author),

    # class Form
    path("contacts", views.ContactFormView.as_view()),  # http://localhost:8000/lesson-fifth/contacts

    # validate
    path("validate", views.UrlView.as_view()),          # # http://localhost:8000/lesson-fifth/validate

]
