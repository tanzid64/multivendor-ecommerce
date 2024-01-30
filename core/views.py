from django.shortcuts import render

# Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsStaffUserOrReadOnly

# Import Serializers
from .serializers import BannerReadSerializer, BannerCreateSerializer

# Model
from .models import Banner

# Create your views here.

class BannerApiView(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    permission_classes = [IsStaffUserOrReadOnly]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BannerReadSerializer
        return BannerCreateSerializer

