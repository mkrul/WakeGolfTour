from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.GolfCourseListView.as_view(),
        name='golf_course_list'),
]
