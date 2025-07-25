from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class FitnessClassListView(generics.ListAPIView):
    queryset = FitnessClass.objects.all().order_by('start_time')
    serializer_class = FitnessClassSerializer
    
    
class BookingCreateView(APIView):
    def post(self,request):
        serializer = BookingSerializer(data= request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        class_id = serializer.validated_data['fitness_class'].id
        fitness_class = get_object_or_404(FitnessClass, id = class_id)
        
        if fitness_class.available_slots <= 0 :
            return Response({"error": "No available slots."}, status=status.HTTP_400_BAD_REQUEST)

        booking = serializer.save()
        fitness_class.available_slots -= 1
        fitness_class.save()
        
        return Response({"message": "Booking successful."}, status=status.HTTP_201_CREATED)


class BookingListByEmailView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_email']
        
