from django.urls import path, include

urlpatterns = [
    path('comments/', include('comments.api.urls')),
    path('protests/', include('protests.api.urls')),
    path('participants/', include('participant.api.urls')),
]
