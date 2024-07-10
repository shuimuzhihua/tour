from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Reservation
from ..serializers import ReservationSerializer


class ReservationListCreateAPIView(APIView):

    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return None

    def get(self, request, pk):
        reservation = self.get_object(pk)
        if reservation is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        if reservation is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservation = self.get_object(pk)
        if reservation is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
