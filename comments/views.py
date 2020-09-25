from django.contrib import messages
from django.views.generic import View, ListView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from protests.models import Protest
from comments.models import Comment


class CommentListView(ListView):

    protest = None
    model = Comment
    context_object_name = 'comments'
    template_name = 'comments/list.html'

    def get_queryset(self):
        protest = get_object_or_404(Protest, slug__iexact=self.kwargs['slug'])
        self.protest = protest
        return Comment.objects.filter(protest=protest)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['protest'] = self.protest
        return context


# noinspection PyMethodMayBeStatic
class CommentDeleteView(LoginRequiredMixin, View):
    login_url = '/user/sign-in/'

    def get(self, request, pk: int):

        comment = get_object_or_404(Comment, pk=pk)
        slug = comment.protest.slug

        if comment.user == request.user:
            comment.delete()
            messages.success(request, 'comment deleted')
        else:
            messages.error(request, 'operation not permitted')

        return redirect('comments:list', slug=slug)


# noinspection PyMethodMayBeStatic
class CommentCreateView(LoginRequiredMixin, View):

    login_url = '/user/sign-in/'

    def post(self, request, pk: int):

        protest = get_object_or_404(Protest, pk=pk)
        content = request.POST.get('content')

        if not content:
            messages.error(request, 'content for comment not provided')
        else:
            Comment.objects.create(protest=protest, user=request.user, content=content)
            messages.success(request, 'comment posted successfully')

        return redirect('comments:list', slug=protest.slug)
