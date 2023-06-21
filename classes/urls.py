from django.urls import path
from . import views


urlpatterns = [
    path('list', views.EnglishClassListAPIView.as_view(), name='classes_list'),
    path('teachers/list', views.TeachersListAPIView.as_view(), name='teachers_list'),
    path('detail/<int:pk>', views.EnglishClassRetrieveAPIView.as_view(), name='class_detail'),
    path('create/form', views.ClassCreateAPIView.as_view(), name='class_create_form'),
    path('update/form/<int:pk>', views.EnglishClassUpdateAPIView.as_view(), name='class_update_form'),
]
