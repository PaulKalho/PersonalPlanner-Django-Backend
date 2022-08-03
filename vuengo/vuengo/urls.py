from django.contrib import admin
from django.urls import path, include

from task.views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('group.urls')),
    path('api/v1/', include('task.urls')),
]
