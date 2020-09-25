from typing import Any, Dict, List

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from protests.models import Protest


def index(request):
    return render(request, 'protests/list.html')


class ProtestDetailView(DetailView):
    model = Protest
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'protest'
    queryset = Protest.objects.all()
    template_name = 'protests/detail.html'


# noinspection PyMethodMayBeStatic
class ProtestCreateView(LoginRequiredMixin, View):

    """ Handles all protest creation logic. """

    login_url = '/user/sign-in/'

    REQUIRED_FIELDS: List[str] = [
        'name',
        'datetime',
        'venue_lat',
        'venue_long',
        'description',
    ]

    def get(self, request):
        return render(request, 'protests/create.html')

    def post(self, request):
        data: Dict[str, Any] = {'organizer': request.user}
        try:
            for field in self.REQUIRED_FIELDS:
                data[field] = request.POST[field]
        except KeyError as field:
            messages.error(request, f'field {str(field)} not provided')
            return render(request, 'protests/create.html', status=400)
        else:
            protest = Protest.objects.create(**data)
            messages.success(
                request, f'organized new event "{data["name"]}" successfully'
            )
            return redirect(protest)
