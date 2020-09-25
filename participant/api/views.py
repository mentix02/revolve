from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from protests.models import Protest
from participant.models import Participant


# noinspection PyMethodMayBeStatic
class ParticipantCreateAPIView(APIView):
    def post(self, request, pk):
        protest = get_object_or_404(Protest, pk=pk)
        protest.add_participant(request.user)
        return Response({'created': True})


# noinspection PyMethodMayBeStatic
class ParticipantDeleteAPIView(APIView):
    def post(self, request, pk):
        qs = Protest.objects.filter(pk=pk).values_list('pk', flat=True)
        if qs.exists():
            Participant.objects.filter(protest_id=qs.get(), user=request.user).delete()
        return Response({'deleted': True})
