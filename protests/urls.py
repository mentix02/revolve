from django.urls import path

from protests.views import index, ProtestCreateView, ProtestDetailView

app_name = 'protests'

urlpatterns = [
    path('', index, name='index'),
    path('create/', ProtestCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', ProtestDetailView.as_view(), name='detail'),
]
