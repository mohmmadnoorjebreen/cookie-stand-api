from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Sport
from .permissions import IsOwnerOrReadOnly
from .serializers import SportSerializer


class SportList(ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class SportDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
