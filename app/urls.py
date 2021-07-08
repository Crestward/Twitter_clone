from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from line import urls as line_urls
from profiles import urls as profile_urls
from followers import urls as follower_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(line_urls, namespace ="line")),
    path('profile/', include(profile_urls, namespace ="profiles")),
    path('follower/', include(follower_urls, namespace ="followers")),
    url("", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
