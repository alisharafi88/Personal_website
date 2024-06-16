from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cnwdjicnweciwcuiwiukhohaha/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('account/', include('accounts.urls', namespace='account')),
    path('message', include('contact_me.urls', namespace='contact_me')),
    path('comment/', include('testimonials.urls', namespace='testimonials')),
    path('i18n/', include('django.conf.urls.i18n')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
