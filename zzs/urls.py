from django.urls import path

from . import views


urlpatterns = [
    path("", views.PlayerView.as_view()),
    path("<int:pk>/", views.PlayerDetailView.as_view()),
    path("player_detail.html", views.BmView.as_view()),

    #path("<slug:slug>/", views.PlayerDetailView.as_view(), name="player_detail"),
]