from rest_framework.serializers import ModelSerializer
from .models import EnglishClass


class EnglishClassSerializer(ModelSerializer):
    class Meta:
        model = EnglishClass
        fields = ('date', 'time_start', 'time_end', 'teacher')

