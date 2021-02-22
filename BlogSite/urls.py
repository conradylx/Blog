from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import index, post, contact, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tinymce/', include('tinymce.urls')),
    path('post/<id>/', post, name="post"),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)