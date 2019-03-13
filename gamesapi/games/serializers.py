from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    played  = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_date)

    def update(self, instance, validated_date):
        instance.name = validated_data.get('name', intsance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = vlaidated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', intsnce.played)
        instance.save()
        return instance   

