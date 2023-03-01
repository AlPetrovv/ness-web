from rest_framework import serializers

from .models import PsychomatrixBaseContent


class SquareOfPythagorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychomatrixBaseContent
        fields = ('code', 'title', 'text',)


class DateSerilizer(serializers.Serializer):
    pass
