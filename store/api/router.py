from django.urls import path
from rest_framework.routers import DefaultRouter
from store.api.views import StoreViewSet, VisitViewSet

router = DefaultRouter()

router.register(r"stores", StoreViewSet, basename="stores")
router.register(r"visit", VisitViewSet, basename="visit")

urlpatterns = router.urls


