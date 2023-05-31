from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import EnglishClass
from users.models import User
from .serializers import EnglishClassSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from django.shortcuts import render, redirect

from datetime import datetime


class EnglishClassListAPIView(ListAPIView):
    queryset = EnglishClass.objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = EnglishClassSerializer

    def get(self, request, *args, **kwargs):
        return Response({'classes': self.get_queryset().filter(date__gte=date.today())}, template_name='classes/homepage.html')


class EnglishClassRetrieveAPIView(RetrieveAPIView):
    queryset = EnglishClass.objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = EnglishClassSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({'class': self.get_object()}, template_name='classes/class_detail.html')


class ClassCreateAPIView(CreateAPIView):
    queryset = EnglishClass.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = EnglishClassSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'classes/class_create_form.html'

    def post(self, request, *args, **kwargs):
        print(request.data)
        class_to_create = {
            'date': datetime.strptime(request.data.get('date'), '%Y-%m-%d').date(),
            'time_start': datetime.strptime(request.data.get('time_start'), '%H:%M').time(),
            'time_end': datetime.strptime(request.data.get('time_end'), '%H:%M').time(),
            'teacher': User.objects.get(pk=request.user.pk)
        }
        EnglishClass.objects.bulk_create([EnglishClass(**class_to_create)])
        return redirect('class_create_form')


class EnglishClassUpdateAPIView(UpdateAPIView):
    pass