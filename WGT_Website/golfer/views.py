from django.shortcuts import render

from django.views import generic
from .models import Golfer

class GolferListView(generic.ListView):
    model = Golfer
    template_name = 'golfer/golfer_list.html'
    context_object_name = 'golfers'

