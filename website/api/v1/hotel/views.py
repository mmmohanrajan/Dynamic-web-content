from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from api.models import Hotel
from .serializers import HotelSerializer


class HotelViewSet(ModelViewSet):
    
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user, images=self.request.data.get('images'))