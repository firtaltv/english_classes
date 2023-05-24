from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import EnglishClass
from .serializers import EnglishClassSerializer
from datetime import date


class EnglishClassListAPIView(ListAPIView):
    queryset = EnglishClass.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EnglishClassSerializer

    def get_queryset(self):
        return super().get_queryset().filter(date__gte=date.today())


class EnglishClassRetrieveAPIView(RetrieveAPIView):
    queryset = EnglishClass.objects.all()
