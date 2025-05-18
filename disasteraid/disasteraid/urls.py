from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),  #  Route root to home app
    path('admin/', admin.site.urls),
    path('preparedness/', include('preparedness.urls')),
    path('realtime/', include('realtime_help.urls')),
    path('reports/', include('realtime_help.urls')),

    path('recovery/', include('recovery.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
