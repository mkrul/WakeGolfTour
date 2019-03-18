from django.shortcuts import render

from django.views import generic
from .models import Golfer, GolferRoundScores

class GolferListView(generic.ListView):
    model = Golfer
    template_name = 'golfer/golfer_list.html'
    context_object_name = 'golfers'

class GolferDetailView(generic.DetailView):
    model = Golfer
    template_name = 'golfer/golfer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GolferDetailView, self).get_context_data(**kwargs)

        golfer = self.get_object()

        context['golfer'] = golfer
        context['scores'] = GolferRoundScores.getTournScoresByGolfer(golfer.golfer_id)

        return context
