from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('u_comment', views.u_comment, name="u_comment"),
]

urlpatterns += staticfiles_urlpatterns()