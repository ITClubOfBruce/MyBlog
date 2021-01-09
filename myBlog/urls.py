from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',include("articles.urls")),
    path('markdownx/', include('markdownx.urls')),
    path('comments/', include('django_comments.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
