from rest_framework import serializers

from .models import *


class Renobe_Serializer(serializers.ModelSerializer):
    tags=serializers.StringRelatedField(many=True)
    class Meta:
        model = Renobe
        fields = "__all__"

class Renobe_chapters_serializers(serializers.ModelSerializer):
    renobe=Renobe_Serializer()
    class Meta:
        model=Renobe_chapters
        fields="__all__"

class Renobe_chapters_list_serializers(serializers.ModelSerializer):
    class Meta:
        model=Renobe_chapters
        fields="__all__"