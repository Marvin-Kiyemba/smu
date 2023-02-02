from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.Serializer):
    asset_name = serializers.CharField(max_length=100)
    assigned_to = serializers.CharField(max_length=100)
    assigned_on = serializers.DateTimeField()
    asset_status = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Record.create(validated_data)

    def update(self, instance, validated_data):
        instance.asset_name = validated_data.get('asset_name', instance.asset_name)
        instance.assiigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.assigned_on = validated_data.get('assigned_on', instance.assigned_on)
        instance.asset_status = validated_data.get('asset_status', instance.asset_status)
        instance.save()
        return instance

