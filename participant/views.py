from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from protests.models import Protest
from participant.models import Participant


# noinspection PyMethodMayBeStatic
class ParticipantCreateView(LoginRequiredMixin, View):
    def get(self, request, pk: int):
        protest = get_object_or_404(Protest, pk=pk)
        protest.add_participant(request.user)
        messages.success(request, f'joined "{protest.name}"')
        return redirect(protest)


# noinspection PyMethodMayBeStatic
class ParticipateDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk: int):
        protest = get_object_or_404(Protest, pk=pk)
        protest.participants.filter(user=request.user).delete()
        messages.error(request, f'left "{protest.name}"')
        return redirect(protest)
