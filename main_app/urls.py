from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name='auth'),
    path('callback/', views.callback, name='callback'),
    path('access', views.access_session, name='access'),
    path('logout', views.logout, name='logout')
]