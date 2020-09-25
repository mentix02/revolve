from typing import List, Dict

from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from user.models import User


# noinspection PyMethodMayBeStatic
class SignInView(View):

    """ Handles all user authentication logic. """

    REQUIRED_FIELDS: List[str] = [
        'username',
        'password',
    ]

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "you're already signed in")
            return redirect('protests:index')
        return render(request, 'user/sign-in.html')

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "you're already signed in")
            return redirect('protests:index')

        data: Dict[str, str] = {}
        try:
            for field in self.REQUIRED_FIELDS:
                data[field] = request.POST[field]
        except KeyError as field:
            messages.error(request, f'field {str(field)} not provided')
            return render(request, 'user/sign-in.html', status=400)
        else:
            user = authenticate(**data)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect('protests:index')
            else:
                messages.error(request, f'invalid credentials provided')
                return render(request, 'user/sign-in.html', status=401)


# noinspection PyMethodMayBeStatic
class SignUpView(View):

    """
    Handles all user sign up logic. get redirects authenticated
    users to index page. post handles unique case insensitive username
    validation (using lower level integrity exception handling).
    """

    REQUIRED_FIELDS: List[str] = [
        'email',
        'username',
        'password',
        'last_name',
        'first_name',
    ]

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "you're already signed in")
            return redirect('protests:index')
        return render(request, 'user/sign-up.html')

    def post(self, request):

        if request.user.is_authenticated:
            messages.info(request, "you're already signed in")
            return redirect('protests:index')

        data: Dict[str, str] = {}

        try:
            for field in self.REQUIRED_FIELDS:
                data[field] = request.POST[field]
        except KeyError as field:
            messages.error(request, f'field {str(field)} not provided')
            return render(request, 'user/sign-up.html', status=400)

        try:
            user = User.objects.create_user(**data)
        except IntegrityError:
            messages.error(request, f'user with username "{data["username"]}" exists.')
            return render(request, 'user/sign-up.html', status=409)
        else:
            login(request, user)
            messages.success(request, f'successfully signed in, {data["username"]}')
            return redirect('protests:index')


# noinspection PyMethodMayBeStatic
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'successfully logged out')
        return redirect('protests:index')
