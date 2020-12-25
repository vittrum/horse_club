from rest_framework import serializers

from api.horse.serializers import HorseSerializer
from api.user.serializers import UserSerializer
from core.models import Schedule, Subscription, ClientSubscription, Plan, Discipline


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    discipline = DisciplineSerializer()

    class Meta:
        model = Subscription
        fields = '__all__'


class ClientSubscriptionSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer()
    client = UserSerializer()

    class Meta:
        model = ClientSubscription
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    trainer = serializers.StringRelatedField()#UserSerializer()
    horse = serializers.StringRelatedField()#HorseSerializer()
    client_subscription = serializers.StringRelatedField()#ClientSubscriptionSerializer()

    class Meta:
        model = Schedule
        fields = '__all__'
