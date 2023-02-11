from rest_framework import serializers
from .models import Record
from assets.models import Asset
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class  AssetSerializer(serializers.ModelSerializer):
    child = RecordSerializer(read_only=True)
    class Meta:
        model = Asset
        fields =  '__all__'
 