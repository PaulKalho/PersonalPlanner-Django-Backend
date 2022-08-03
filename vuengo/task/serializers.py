from rest_framework import serializers

from .models import Task

#Get json data in easier way -> Serializer


# WHAT IS THE DIFFERENCE BETWEEN THE DIFFERENT SERIALIZERS (z.B ModelSerializer oder HyperlinekdSerializer???)
    # HyperlinkedSerialzier uses hyperlinks to represent relationships
    # ModelSerlializer uses key to represent relationships!!! 


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = (
            'created_by',
        )
        fields = (
            'id' ,
            'description', 
            'status', 
            'group',
            'created_by',
            'date'
        )