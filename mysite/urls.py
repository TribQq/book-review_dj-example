"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    # book_review urls
    path('', include('book_review.urls')),
    # users urls
    path('', include('users.urls'))
]

if settings.DEBUG:
    from django.contrib.staticfiles.views import serve
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # маршрут для обработки выгруженных файлов
else: # only for heroku , if deploy + nginx/apache need refactor
    from django.views.static import serve as serve
    urlpatterns.extend([
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),   
    ])
    