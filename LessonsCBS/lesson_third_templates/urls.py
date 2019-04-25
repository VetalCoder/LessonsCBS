from django.urls import path
from . import views

urlpatterns = [
    path('view', views.view),
    
    path('filters', views.filter),    
    path('tags-if', views.tags_if),
    path('tags-for', views.tags_for),
    path('tags-regroup', views.tag_regroup),
    
    path('base', views.base),
    path('adrian', views.adrian),
    path('releases', views.releases),
    ]
