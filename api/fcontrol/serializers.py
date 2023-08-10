from rest_framework import serializers
from fcontrol.models import Institution, Controller, ControllerData
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate
class InstitutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id','name','address']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()




class SensorDataSerializer(serializers.Serializer):

    # controlle_id дописать
    controller_id = serializers.IntegerField(default=1)
    temperature = serializers.DecimalField(max_digits=5, decimal_places=2, min_value=-60, max_value=80)
    humidity = serializers.IntegerField(min_value=0, max_value=100)
    def save(self):
        controller = Controller.objects.get(id=self.validated_data['controller_id'])
        controller_data = ControllerData.objects.create(
            controller= controller,
            temperature = self.validated_data['temperature'],
            humidity = self.validated_data['humidity'],
        )
        new_sensor_data = {
            'institution': controller.institution.id,
            'sensor_id': controller.id,
            'temperature': str(controller_data.temperature),
            'humidity': controller_data.humidity,
        }
        data = {
            'type': 'sensor_data_handler',
            'data': new_sensor_data,

                }
        async_to_sync(get_channel_layer().group_send)('sensor_data', data)

        # print(self.validated_data)
        # print(controller)
        return controller_data
