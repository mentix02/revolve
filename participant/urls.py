from django.urls import path

from participant.views import ParticipantCreateView, ParticipateDeleteView

app_name = 'participant'

urlpatterns = [
    path('create/<int:pk>/', ParticipantCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ParticipateDeleteView.as_view(), name='delete'),
]
