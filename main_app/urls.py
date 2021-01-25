from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name='auth'),
    path('callback/', views.callback, name='callback'),
    path('access', views.access_session, name='access'),
    path('logout', views.logout, name='logout'),
    path('tourney/', views.tourney_index, name='tourney_index'),
    path('tourney/<int:tourney_id', views.tourney_show, name='tourney_show'),
    path('tourney/create/', views.tourney_create, name='tourney_create')
]