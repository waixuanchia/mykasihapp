from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import officerViewSet,roleViewSet

router = DefaultRouter()
router.register("officers",officerViewSet)
router.register("roles",roleViewSet)

urlpatterns = [
    path("",include(router.urls)),
]
