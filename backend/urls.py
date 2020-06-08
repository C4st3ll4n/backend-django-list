from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import GroupViewSet, UserViewSet
from core.views import ListViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet)
router.register(r'item', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
