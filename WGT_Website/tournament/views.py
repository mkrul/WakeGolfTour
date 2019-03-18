from django.shortcuts import render

from django.views import generic
from .models import Tournament

class TournamentListView(generic.ListView):
    model = Tournament
    template_name = 'tournament/tournament_list.html'
    context_object_name = 'tournaments'
