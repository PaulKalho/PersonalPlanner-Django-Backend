from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        read_only_fields = (
            'created_by',
        )
        fields = (
            'id',
            'description',
            'created_by'
        )
