from typing import List, Dict

from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from user.models import User

SIGN_IN_REQUIRED_FIELDS: List[str] = [
    'username',
    'password',
]

SIGN_UP_REQUIRED_FIELDS: List[str] = [
    'email',
    'username',
    'password',
    'last_name',
    'first_name',
]


# noinspection PyMethodMayBeStatic
class SignInView(View):
    def get(self, request):
        return render(request, 'user/sign-in.html')

    def post(self, request):
        return render(request, 'user/sign-in.html')


# noinspection PyMethodMayBeStatic
class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "you're already signed in")
            return redirect('protests:index')
        return render(request, 'user/sign-up.html')

    def post(self, request):
        data: Dict[str, str] = {}
        try:
            for field in SIGN_UP_REQUIRED_FIELDS:
                data[field] = request.POST[field]
        except KeyError as field:
            messages.error(request, f'field {str(field)} not provided')
            return render(request, 'user/sign-up.html', status=400)

        try:
            user = User.objects.create_user(**data)
        except IntegrityError:
            print('')


# noinspection PyMethodMayBeStatic
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'successfully logged out')
        return redirect('protests:index')
