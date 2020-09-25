from django.urls import path

from comments.views import CommentListView, CommentCreateView, CommentDeleteView

app_name = 'comments'

urlpatterns = [
    path('list/<slug:slug>/', CommentListView.as_view(), name='list'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='delete'),
    path('create/<int:pk>/', CommentCreateView.as_view(), name='create'),
]
