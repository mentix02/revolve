from django.urls import path

from user.views import LogoutView, SignInView, SignUpView, UserDetailView

app_name = 'user'

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('detail/<slug:username>/', UserDetailView.as_view(), name='detail'),
]
