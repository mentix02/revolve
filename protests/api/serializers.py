from rest_framework import serializers

from protests.models import Protest


class ProtestSerializer(serializers.ModelSerializer):

    organizer = serializers.StringRelatedField()

    class Meta:
        model = Protest
        fields = '__all__'
