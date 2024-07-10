from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'rv_date', 'tr_id', 'rt_rq_id', 'status']

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rv_date = validated_data.get('rv_date', instance.rv_date)
        instance.tr_id = validated_data.get('tr_id', instance.tr_id)
        instance.rt_rq_id = validated_data.get('rt_rq_id', instance.rt_rq_id)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
