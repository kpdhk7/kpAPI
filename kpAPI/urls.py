"""kpAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include, handler500
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from bankinfo import views as bi_views

app_name = "bankinfo"

urlpatterns = [
    url(r'api/read/', bi_views.read, name='read'),
    url(r'api/devices/',bi_views.deviceinfo, name='devices'),
    url(r'api/mostallyear/',bi_views.mostallyear, name='mostallyear'),
    url(r'api/mostinyear/',bi_views.mostinyear, name='mostinyear'),
    url(r'api/mostindevice/',bi_views.mostindevice, name='mostindevice'),
#    url(r'api/predictdevice/',bi_views.predictdevice),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]
