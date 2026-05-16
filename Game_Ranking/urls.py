from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import TemplateView


def favicon(request):
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#0f1117"/>'
        '<path d="M18 24h28a10 10 0 0 1 9 14l-2 5a7 7 0 0 1-12 2l-3-4H26l-3 4a7 7 0 0 1-12-2l-2-5a10 10 0 0 1 9-14Z" fill="#6dc2ff"/>'
        '<circle cx="44" cy="32" r="3" fill="#08111b"/>'
        '<circle cx="51" cy="36" r="3" fill="#08111b"/>'
        '<path d="M19 33h12M25 27v12" stroke="#08111b" stroke-width="4" stroke-linecap="round"/>'
        '</svg>'
    )
    return HttpResponse(svg, content_type='image/svg+xml')


urlpatterns = [
        path('admin/', admin.site.urls),
        path('favicon.ico', favicon, name='favicon'),
        path('google91eb3706ff299c8c.html', TemplateView.as_view(template_name='google91eb3706ff299c8c.html', content_type='text/html')),
        path('', include('games.urls')),
        path('reviews/', include('reviews.urls')),
        path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
