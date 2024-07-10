from rest_framework import serializers
from .models import Rt_Rq


class Rt_RqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rt_Rq
        fields = ['id', 'rt_id', 'rq', 'days']

    def create(self, validated_data):
        return Rt_Rq.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rt_id = validated_data.get('rt_id', instance.rt_id)
        instance.rq = validated_data.get('rq', instance.rq)
        instance.days = validated_data.get('days', instance.days)
        instance.save()
        return instance
