from django.urls import path,include
from rest_framework import routers
from .views import ReportViewSet

router = routers.DefaultRouter()
router.register("reports",ReportViewSet)

urlpatterns = [
    path("",include(router.urls))
]