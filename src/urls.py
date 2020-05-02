from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    url(r'^', include('django_telegrambot.urls')),
]
