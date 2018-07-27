# Api
from django.urls import path, include

urlpatterns = [
    path('api/posts/', include('posts.urls.apis')),
    path('api/users/', include('members.urls.apis')),
]
