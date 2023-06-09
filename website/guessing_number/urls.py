from django.urls import path
from . import views

urlpatterns = [
    path('play/',views.index,name="game_1"),
    path('result',views.result),
    path('clear',views.clear),
    path('submit_username',views.submit_username),
    path('play/leaderboard',views.leaderboard)
]
