from rest_framework import serializers
from .models import FitnessClass, Booking
from django.utils.timezone import localtime

class FitnessClassSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'start_time', 'instructor', 'available_slots']
        
    def get_start_time(self,obj):
        return localtime(obj.start_time).strftime('%Y-%m-%d %H:%M')
    
    
class BookingSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(required=True, min_length=2)
    client_email = serializers.EmailField(required=True)
    fitness_class = serializers.PrimaryKeyRelatedField(queryset=FitnessClass.objects.all())

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        fitness_class = data['fitness_class']
        client_email = data['client_email']

        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("No slots available for this class.")

        if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
            raise serializers.ValidationError("You have already booked this class.")

        return data
    