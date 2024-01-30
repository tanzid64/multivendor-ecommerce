from rest_framework import serializers

# Models
from .models import Banner

class BannerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class BannerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        exclude = ['slug']