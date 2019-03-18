from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.TournamentListView.as_view(),
        name='tournament_list'),
    url('<int:pk>/', views.TournamentDetailView.as_view(),
        name='tournament_detail')
]
