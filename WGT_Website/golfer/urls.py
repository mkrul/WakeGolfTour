from django.conf.urls import url
from . import views

urlpatterns = [ 
    url('', views.GolferListView.as_view(),
        name='golfer_list'),
    url('<int:pk>/',views.GolferDetailView.as_view(),name='golfer_detail')
]

