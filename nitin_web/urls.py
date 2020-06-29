from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('video/', include('video.urls'))
]
