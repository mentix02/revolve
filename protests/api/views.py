from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from protests.models import Protest
from protests.api.serializers import ProtestSerializer


class ProtestListAPIView(ListAPIView):
    serializer_class = ProtestSerializer
    pagination_class = PageNumberPagination
    queryset = Protest.objects.order_by('-timestamp')
