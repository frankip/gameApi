from django.conf.urls import url
from django.urls import path
from games.views import (
    GameCategoryList,
    GameCategoryDetail,
    GameList,
    GameDetail,
    PlayerList,
    PlayerDetail,
    PlayerScoreList,
    PlayerScoreDetail,
    ApiRoot
)

urlpatterns = [
    path('games', GameList.as_view(), name=GameList.name),
    path('games/<int:pk>/', GameDetail.as_view(), name=GameDetail.name),
    path('game-categories', GameCategoryList.as_view(), name=GameCategoryList.name),
    path('game-categories/<int:pk>/', GameCategoryDetail.as_view(), name=GameCategoryDetail.name),
    path('players', PlayerList.as_view(), name=PlayerList.name),
    path('players/<int:pk>/', PlayerDetail.as_view(), name=PlayerDetail.name),
    path('player-scores', PlayerScoreList.as_view(), name=PlayerScoreList.name),
    path('player-scores/<int:pk>/', PlayerScoreDetail.as_view(), name=PlayerScoreDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),

]
