from django.urls import path, re_path, include
from . import views

# http://localhost:8000/lesson-two-part2/50-asd/history/
urlpatterns = [
    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/history/$', views.history),
    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/edit/$', views.edit),
    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/discuss/$', views.discuss),
    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>\w+)/permissions/$', views.permissions),
]


# http://localhost:8000/lesson-two-part2/50-asd/history/
#urlpatterns = [
#    re_path(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\w]+)/', include([
#        path('history/', views.history),
#        path('edit/', views.edit),
#        path('discuss/', views.discuss),
#        path('permissions/', views.permissions),
#    ])),
#]


#extra_patterns = [
#    path('report/', views.report),
#    re_path(r'^report/(?P<id>[0-9]+)/$', views.report),
#]

#urlpatterns = [
#    re_path(r'blog/(page-(\d+)/)?$', views.blog_articles),                                  # bad   http://localhost:8000/lesson-two-part2/blog/page-2/
#    re_path(r'comments/(?:page-(?P<page_number>\d+)/)?$',views.comments),                   # good  http://localhost:8000/lesson-two-part2/comments/page-2/
#    re_path(r'^optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}),   # http://localhost:8000/lesson-two-part2/optional-args/2222/
#    path('extra/' , include(extra_patterns)),                                               # http://localhost:8000/lesson-two-part2/extra/report/
#]
