from rest_framework import serializers

from horse.models import Horse
from user.models import Owner


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'


class OwnerDetailSerializer(serializers.ModelSerializer):
    horses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = '__all__'
