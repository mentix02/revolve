from django.urls import path

from protests.api.views import ProtestListAPIView

app_name = 'protests_api'

urlpatterns = [
    path('list/', ProtestListAPIView.as_view(), name='list'),
]
