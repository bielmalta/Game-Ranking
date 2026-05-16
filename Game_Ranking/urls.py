from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
        path('admin/', admin.site.urls),
        path(
                'favicon.ico',
                RedirectView.as_view(
                        url=f'{settings.STATIC_URL}games/img/game-ranking-icon.png',
                        permanent=True,
                ),
                name='favicon',
        ),
        path('google91eb3706ff299c8c.html', TemplateView.as_view(template_name='google91eb3706ff299c8c.html', content_type='text/html')),
        path('', include('games.urls')),
        path('reviews/', include('reviews.urls')),
        path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
