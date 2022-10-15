from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        field = ['id', 'title', 'artist', 'album', 'release_date', 'genre', 'likes']