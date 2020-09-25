from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from protests.models import Protest
from comments.models import Comment


# noinspection PyMethodMayBeStatic
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):

        protest = get_object_or_404(Protest, pk=pk)
        content = request.POST.get('content')

        if not content:
            messages.error(request, 'content for comment not provided')
        else:
            Comment.objects.create(protest=protest, user=request.user)
            messages.success(request, 'comment posted successfully')

        return redirect(protest)
