# from rest_framework.parsers import JSONParser 
# from rest_framework import status 
# from rest_framework.decorators import api_view 
# from rest_framework.response import Response

# # models
# from games.models import Game

# # serializers
# from games.serializers import GameSerializer


# # Create your views here.

# @api_view(['GET', 'POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many=True)
#         return Response(games_serializer.data)
#     elif request.method == 'POST':
#         game_serializer = GameSerializer(data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data,
#             status=status.HTTP_201_CREATED)
#         return Response(game_serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'POST']) 
# def game_detail(request, pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data)
#         return Response(game_serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 

""" Class based views"""
import django_filters
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters 
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter 

from games.models import (
    GameCategory,
    Game,
    Player,
    PlayerScore)
from games.serializers import(
    UserSerializer,
    GameCategorySerializer,
    GameSerializer,
    PlayerSerializer,
    PlayerScoreSerializer 
)
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView
)

from games.permissions import IsOwnerOrReadOnly


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    name = 'user-detail'


class GameCategoryList(ListCreateAPIView):
    queryset = GameCategory.objects.all() 
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_class = (ScopedRateThrottle)
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class GameCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'
    throttle_scope = 'game-categories'
    throttle_class = (ScopedRateThrottle)


class GameList(ListCreateAPIView):
    queryset = Game.objects.all() 
    serializer_class = GameSerializer 
    name = 'game-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    filter_fields = (
        'name',
        'game_category',
        'release_date',
        'played',
        'owner',
        )
    search_fields = ('^name',)
    ordering_fields = ('name', 'release_date')

    def perform_create(self, serializer):
        # Pass an additional owner field to the create method 
        # To Set the owner to the user received in the request
        serializer.save(owner=self.request.user)


class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

class PlayerList(ListCreateAPIView): 
    queryset = Player.objects.all() 
    serializer_class = PlayerSerializer 
    name = 'player-list'
    filter_fields = ('name', 'gender',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class PlayerDetail(RetrieveUpdateDestroyAPIView): 
    queryset = Player.objects.all() 
    serializer_class = PlayerSerializer 
    name = 'player-detail'

class PlayerScoreFilter(django_filters.FilterSet):
    min_score = NumberFilter(field_name='score', lookup_expr='gte')
    max_score = NumberFilter(field_name='score', lookup_expr='lte')
    from_score_date = DateTimeFilter(field_name='score_date', lookup_expr='gte')
    to_score_date = DateTimeFilter(field_name='score_date', lookup_expr='lte')
    player_name = AllValuesFilter(field_name='player__name')
    game_name = AllValuesFilter(field_name='game__name')

    class Meta:
        model = PlayerScore 
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            # #player__name will be accessed as player_name 
            'player_name',
            # #game__name will be accessed as game_name 
            'game_name',
            ) 

class PlayerScoreList(ListCreateAPIView): 
    queryset = PlayerScore.objects.all() 
    serializer_class = PlayerScoreSerializer 
    name = 'playerscore-list'
    filter_class = PlayerScoreFilter
    ordering_fields = ('score', 'score_date',)

class PlayerScoreDetail(RetrieveUpdateDestroyAPIView): 
    queryset = PlayerScore.objects.all() 
    serializer_class = PlayerScoreSerializer 
    name = 'playerscore-detail' 

class ApiRoot(GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request)
        })
        