from django.urls import path
from . import views


urlpatterns = [
    path('list', views.EnglishClassListAPIView.as_view(), name='classes_list'),
    path('detail/<int:pk>', views.EnglishClassRetrieveAPIView.as_view(), name='class_detail'),
    path('create', views.ClassCreateAPIView.as_view(), name='class_create'),
    path('create/form', views.ClassCreateAPIView.as_view(), name='class_create_form'),
]
