from django.urls import path

from protests.views import index

app_name = 'protests'

urlpatterns = [
    path('', index, name='index'),
]
