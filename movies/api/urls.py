from django.conf.urls import url

from api.views import MovieCreateView, MovieDetailView

urlpatterns = [
    url(r'^movies/$', MovieCreateView.as_view(), name='movies'), #api/v1/movies/$
    url(r'^movies/(?P<pk>[0-9]+)$', MovieDetailView.as_view(), name='detail'),
]