from django.urls import path
from .views import List

urlpatterns = [
    path("", List.as_view(), name='list-view'),        # http://localhost:8000/lesson-sixth/
]


