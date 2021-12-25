from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from store.api.serializers import StoreSerializer, VisitSerializer
from store.models import Store, Visit


class StoreViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(employee__phone=self.request.auth)


class VisitViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = VisitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Visit.objects.filter(store__employee__phone=self.request.auth)
