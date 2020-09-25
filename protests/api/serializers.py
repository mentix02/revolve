from rest_framework.serializers import ModelSerializer

from protests.models import Protest


class ProtestSerializer(ModelSerializer):
    class Meta:
        model = Protest
        fields = '__all__'
