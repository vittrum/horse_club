from rest_framework import serializers

from horse.models import Horse


class HorseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horse
        fields = '__all__'

