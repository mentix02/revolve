from django.urls import path

from protests.views import (
    ProtestListView,
    ProtestEditView,
    ProtestDetailView,
    ProtestCreateView,
    ProtestDeleteView,
    DashboardListView,
)

app_name = 'protests'

urlpatterns = [
    path('', ProtestListView.as_view(), name='index'),
    path('create/', ProtestCreateView.as_view(), name='create'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('edit/<slug:slug>/', ProtestEditView.as_view(), name='edit'),
    path('delete/<slug:slug>/', ProtestDeleteView.as_view(), name='delete'),
    path('detail/<slug:slug>/', ProtestDetailView.as_view(), name='detail'),
]
