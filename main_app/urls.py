from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name='auth'),
    path('callback/', views.callback, name='callback'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('tournament/', views.tournament_index, name='tournament_index'),
    path('tournament/<int:tournament_id>', views.tournament_show, name='tournament_show'),
    path('tournament/create/', views.tournament_create, name='tournament_create'),
    path('tournament/create/teams', views.tournament_teams, name='tournament_teams'),
    path('tournament/create/teams/set', views.tournament_teams_set, name='tournament_teams_set'),
]