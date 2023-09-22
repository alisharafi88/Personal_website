from .models import Comment


def comments(request):
    comments = Comment.objects.filter(is_active=True)
    return {'comments': comments}
