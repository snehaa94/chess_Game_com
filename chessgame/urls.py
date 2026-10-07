from django.urls import path
from chessgame.game import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/new-game/', views.new_game, name='new_game'),
    path('api/state/', views.state, name='state'),
    path('api/move/', views.move, name='move'),
    path('api/health/', views.health, name='health'),
]
