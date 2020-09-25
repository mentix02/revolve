from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from protests.models import Protest
from comments.api.serializers import CommentSerializer


# noinspection PyMethodMayBeStatic
class CommentCreateAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, pk: int):
        protest = get_object_or_404(Protest, pk=pk)
        comment = Comment.objects.create(protest=protest, user=request.user)
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
