from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render

from .models import Player, Team


class PlayerView(ListView):
    """Список професиональных игроков"""
    model = Player
    queryset = Player.objects.all()


class PlayerDetailView(DetailView):
    """Игрок"""
    def get(self, request, pk):
        player = Player.objects.all(id=pk)
        return render(request, "zzs/player_detail.html", {"player": player})


class BmView(ListView):
    """Bm"""
    model = Player
    queryset = Player.objects.all()
    template_name = "zzs/player_detail.html"
