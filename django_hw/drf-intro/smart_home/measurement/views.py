# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# 1, 4
class SensorView(ListCreateAPIView):
    """Список датчиков / Добавить датчик"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 2, 5
class SensorDetailView(RetrieveUpdateAPIView):
    """Получить данные по датчику / Изменить данные по датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# 3
class MeasurementCreateView(CreateAPIView):
    """Добавить температуру"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверка на валидность данных
        self.perform_create(serializer)  # Сохраняем данные
        return Response(serializer.data, status=201)  # Возвращаем данные с статусом 201

