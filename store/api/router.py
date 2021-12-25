from django.urls import path
from rest_framework.routers import DefaultRouter

from store.api.views import StoreViewSet, VisitView

router = DefaultRouter()

router.register(r'stores', StoreViewSet, basename='stores')

urlpatterns = router.urls

urlpatterns += [
    path('visit', VisitView.as_view(), name='visit')
]
