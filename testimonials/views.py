from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CreateCommentForm


def create_comment_view(request):
    form = CreateCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        messages.success(
            request,
            _(f'{request.user.username}, You sent your comment successfully!'),
            'success',
        )
        return redirect('home:home')
    messages.error(request, _('Something wrong happened! Try again.'), 'danger')
    return redirect('home:home')
