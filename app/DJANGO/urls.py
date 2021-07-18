"""DJANGO URL Configuration

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
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from APP_users.api import register_new_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # ADMIN PANEL
    path('admin/', admin.site.urls),

    # AUTH
    path('auth/api/login/', obtain_auth_token, name='login'),
    path('auth/api/register/', register_new_user, name='register'),
]

# APPEND: url mapping for media files
## allows access to media files while running the development server
## in prodution NGINX will handle this do only run if DEBUG=TRUE
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


