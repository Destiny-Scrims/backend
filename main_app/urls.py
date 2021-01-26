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
    path('tournament/create/teams', views.tournament_create_teams, name='tournament_teams'),
    path('tournament/create/teams/set', views.tournament_create_teams_set, name='tournament_teams_set'),
    path('tournament/delete/<int:tournament_id>', views.tournament_delete, name='tournament_delete'),
    path('tournament/update/<int:tournament_id>', views.tournament_update, name='tournament_update'),
    path('tournament/update/teams/<int:tournament_id>', views.tournament_update_teams, name='tournament_update_teams'),
    path('tournament/update/teams/set/<int:tournament_id>', views.tournament_update_teams_set, name='tournament_update_teams_set'),
]