from django.urls import path
from .views import FitnessClassListView, BookingCreateView, BookingListByEmailView

urlpatterns = [
    path('classes/', FitnessClassListView.as_view(), name='classes'),
    path('book/', BookingCreateView.as_view(), name='book-class'),
    path('bookings/', BookingListByEmailView.as_view(), name='booking-by-email'),
]

