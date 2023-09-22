from .models import Blog


def blogs(request):
    blogs = Blog.objects.filter(is_active=True)
    return {'blogs': blogs}
