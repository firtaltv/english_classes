from rest_framework.serializers import ModelSerializer
from .models import EnglishClass
from users.models import User


class EnglishClassSerializer(ModelSerializer):
    class Meta:
        model = EnglishClass
        fields = ('date', 'time_start', 'time_end', 'teacher', 'level')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'age', 'status')
