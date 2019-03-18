from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.TournamentListView.as_view(),
        name='tournament_list'),
]
