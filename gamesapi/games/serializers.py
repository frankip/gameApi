# from rest_framework import serializers
# from games.models import Game

# class GameSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     release_date = serializers.DateTimeField()
#     played  = serializers.BooleanField(required=False)

#     def create(self, validated_data):
#         return Game.objects.create(**validated_data)

#     def update(self, instance, validated_date):
#         instance.name = validated_data.get('name', intsance.name)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.game_category = vlaidated_data.get('game_category', instance.game_category)
#         instance.played = validated_data.get('played', intsnce.played)
#         instance.save()
#         return instance 
from rest_framework import serializers
from games.models import (Game, GameCategory, Player, PlayerScore)
from django.contrib.auth.models import User
import games.views


class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'games'
        )
class GameCategorySerializer(serializers.HyperlinkedModelSerializer): 
    games = serializers.HyperlinkedRelatedField( 
        many=True, 
        read_only=True, 
        view_name='game-detail') 
 
    class Meta: 
        model = GameCategory 
        fields = (
            'url',
            'pk',
            'name', 
            'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # We want to display the game cagory's name instead of the id 
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name') 

    class Meta:
        model = Game
        fields = (
            'url',
            'owner',
            'game_category',
            'name',
            'release_date',
            'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    # We want to display all the details for the game 
    game = GameSerializer()
    # We don't include the player because it will be nested in the player

    class Meta: 
        model = PlayerScore
        fields = (
            'url',
            'owner',
            'pk',
            'score',
            'score_date',
            'game',
            )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta: 
        model = Player 
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
            )


class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    # We want to display the game's name instead of the id
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore 
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
            )
