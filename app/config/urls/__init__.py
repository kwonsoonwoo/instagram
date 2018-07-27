from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .. import views

from django.contrib import admin

urlpatterns = [
    # View
    path('', include('config.urls.views')),
    # Api
    path('api/', include('config.urls.apis')),

]
