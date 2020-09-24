from django.urls import path

from user.views import SignInView, SignUpView

app_name = 'user'

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
