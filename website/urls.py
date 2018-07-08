from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^$', include('music.urls')),
]
