from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dev/admin/', admin.site.urls),
    path('', include('users.urls')),
    # path('admin/', admin.site.urls),
    # path('activities/', include('users.urls')),
    # path('moderation/', include('users.urls')),
]


if settings.DEBUG:
    from django.conf.urls import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    if settings.MEDIA_ROOT:
        urlpatterns += static.static(
            prefix=settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    
    urlpatterns += staticfiles_urlpatterns()
