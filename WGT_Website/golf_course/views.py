from django.shortcuts import render

from django.views import generic
from .models import GolfCourse

class GolfCourseListView(generic.ListView):
    model = GolfCourse
    template_name = 'golf_course/golf_course_list.html'
    context_object_name = 'golf_courses'
