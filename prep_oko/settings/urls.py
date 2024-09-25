from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dev/admin/', admin.site.urls),
    path('users/', include(
        'users.urls',
        namespace='users',
    )),
    path('activities/', include(
        'activities.urls',
        namespace='activities',
    )),
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
