from django.urls import path,include
from rest_framework import routers
from .views import ReportViewSet,StatusViewSet

router = routers.DefaultRouter()
router.register("reports",ReportViewSet)
router.register("status",StatusViewSet)

urlpatterns = [
    path("",include(router.urls)),

]