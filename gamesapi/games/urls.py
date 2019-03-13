from django.conf.urls import url
from django.urls import path
from games import views

urlpatterns = [
    path('games', views.game_list),
    path('games/(?P<pk>[0-9]+)/$', views.game_detail)
]
