from rest_framework import mixins, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from store.api.serializers import StoreSerializer, VisitSerializer
from store.models import Store


class StoreViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Store.objects.filter(employee__phone=self.request.auth)


class VisitView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
