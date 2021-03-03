from .models import SoundCoreModel
from rest_framework import serializers


class SoundCoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundCoreModel
        fields = "__all__"
