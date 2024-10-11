from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    sensor = serializers.SlugRelatedField(slug_field='name', queryset=Sensor.objects.all())  # Отображаем имя датчика, а не его ID

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']  # Добавлено поле created_at

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
