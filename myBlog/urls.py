from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',include("articles.urls")),
    path('markdownx/', include('markdownx.urls')),
    path('comments/', include('django_comments.urls')),
]
