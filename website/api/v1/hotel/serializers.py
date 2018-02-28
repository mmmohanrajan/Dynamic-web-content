from rest_framework import serializers

from api.models import User, Hotel


class HotelSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Hotel
        fields = '__all__'
        read_only_fields = ('uploaded_by',)