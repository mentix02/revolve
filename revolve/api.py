from django.urls import path, include

urlpatterns = [
    path('protests/', include('protests.api.urls')),
]
