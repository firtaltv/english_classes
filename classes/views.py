from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import EnglishClass
from users.models import User
from .serializers import EnglishClassSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .mixins import ClassValidationMixin
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT, HTTP_400_BAD_REQUEST
from rest_framework.request import Request
from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime, date


class EnglishClassListAPIView(ListAPIView):
    queryset = EnglishClass.objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = EnglishClassSerializer

    def get(self, request, *args, **kwargs):
        print(self.get_queryset())
        return Response({'classes': self.get_queryset()}, template_name='classes/classes_list.html')


class EnglishClassRetrieveAPIView(RetrieveAPIView):
    queryset = EnglishClass.objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = EnglishClassSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({'class': self.get_object()}, template_name='classes/class_detail.html')


class ClassCreateAPIView(ListCreateAPIView, ClassValidationMixin):
    queryset = EnglishClass.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = EnglishClassSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'classes/class_create_form.html'

    def post(self, request, *args, **kwargs):
        print(request.data)
        if request.data.get('teacher'):
            pk = request.data.get('teacher')
        else:
            pk = request.user.pk
        class_to_create = {
            'date': datetime.strptime(request.data.get('date'), '%Y-%m-%d').date(),
            'time_start': datetime.strptime(request.data.get('time_start'), '%H:%M').time(),
            'time_end': datetime.strptime(request.data.get('time_end'), '%H:%M').time(),
            'teacher': User.objects.get(pk=pk)
        }
        response = self.validate(class_to_create, request.user.pk, request, self.get_queryset())
        if response:
            return Response({'exc': response.data})
        EnglishClass.objects.bulk_create([EnglishClass(**class_to_create)])
        return redirect('class_create_form')


class EnglishClassUpdateAPIView(UpdateAPIView, ClassValidationMixin):
    queryset = EnglishClass.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = EnglishClassSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'classes/class_update_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exc = None

    def get(self, request, pk):
        inst = get_object_or_404(EnglishClass, pk=pk)
        serializer = EnglishClassSerializer(inst)
        return Response({'serializer': serializer, 'inst': inst, 'exc': self.exc})

    def post(self, request, pk, *args, **kwargs):
        inst = get_object_or_404(EnglishClass, pk=pk)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'inst': inst})
        class_to_update = {
            'date': datetime.strptime(serializer.data.get('date'), '%Y-%m-%d').date(),
            'time_start': datetime.strptime(serializer.data.get('time_start'), '%H:%M:%S').time(),
            'time_end': datetime.strptime(serializer.data.get('time_end'), '%H:%M:%S').time(),
            'teacher': serializer.data.get('teacher')
        }
        response = self.validate(class_to_update, request.user.pk, request, self.get_queryset())
        print(response.data)
        if response:
            self.exc = response.data
            return Response({'serializer': serializer, 'inst': inst, 'exc': self.exc})
        self.update_class(request, serializer.validated_data, pk)
        return redirect('classes_list')

    def update_class(self, request, data, pk):
        lesson = EnglishClass.objects.get(pk=pk)
        lesson.date = data.get('date')
        lesson.time_start = data.get('time_start')
        lesson.time_end = data.get('time_end')
        EnglishClass.objects.bulk_update([lesson], ['date', 'time_start', 'time_end'])
