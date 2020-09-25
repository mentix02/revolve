from django.urls import path

from participant.api.views import ParticipantCreateAPIView, ParticipantDeleteAPIView

app_name = 'participant_api'

urlpatterns = [
    path('create/<int:pk>/', ParticipantCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', ParticipantDeleteAPIView.as_view(), name='delete'),
]
