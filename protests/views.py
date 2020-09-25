from typing import Any, Dict, List

from django.contrib import messages
from django.views.generic import View, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from protests.models import Protest


def index(request):
    return render(request, 'protests/list.html')


class DashboardListView(LoginRequiredMixin, TemplateView):
    login_url = '/user/sign-in/'
    template_name = 'user/dashboard.html'


class ProtestDetailView(DetailView):
    model = Protest
    slug_url_kwarg = 'slug'
    slug_field = 'slug__iexact'
    context_object_name = 'protest'
    queryset = Protest.objects.all()
    template_name = 'protests/detail.html'


# noinspection PyMethodMayBeStatic
class ProtestEditView(LoginRequiredMixin, View):

    login_url = '/user/sign-in/'
    FIELDS: List[str] = [
        'name',
        'timestamp',
        'venue_lat',
        'venue_long',
        'description',
    ]

    def get(self, request, slug):
        protest = get_object_or_404(Protest, slug__iexact=slug)
        if request.user.id == protest.organizer_id:
            return render(request, 'protests/edit.html', {'protest': protest})

    def post(self, request, slug):
        protest = get_object_or_404(Protest, slug__iexact=slug)
        if request.user.id == protest.organizer_id:
            for field in self.FIELDS:
                setattr(
                    protest, field, request.POST.get(field, getattr(protest, field))
                )
            protest.save()
            messages.info(request, f'event "{protest.name}" successfully updated')
        else:
            messages.error(request, 'operation not permitted')
        return redirect(protest)


# noinspection PyMethodMayBeStatic
class ProtestDeleteView(LoginRequiredMixin, View):

    login_url = '/user/sign-in/'

    def get(self, request, slug):
        protest = get_object_or_404(Protest, slug__iexact=slug)
        if request.user.id == protest.organizer_id:
            protest.delete()
            messages.success(request, 'event deleted successfully')
            return redirect('protests:index')
        else:
            messages.error(request, 'operation not permitted')
            return redirect(protest)


# noinspection PyMethodMayBeStatic
class ProtestCreateView(LoginRequiredMixin, View):

    """ Handles all protest creation logic. """

    login_url = '/user/sign-in/'

    REQUIRED_FIELDS: List[str] = [
        'name',
        'timestamp',
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
