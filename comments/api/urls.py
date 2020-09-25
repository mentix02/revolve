from django.urls import path

from comments.api.views import CommentCreateAPIView

app_name = 'comments_api'

urlpatterns = [
    path('create/', CommentCreateAPIView.as_view(), name='create'),
]
