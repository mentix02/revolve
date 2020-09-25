from rest_framework.generics import ListAPIView

from protests.models import Protest
from protests.api.serializers import ProtestSerializer


class ProtestListAPIView(ListAPIView):
    queryset = Protest.objects.all()
    serializer_class = ProtestSerializer
