from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from . import views 
import debug_toolbar

urlpatterns = [
    path('', views.index, name='index'),
    path('newPost', views.newPost, name='newPost'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns