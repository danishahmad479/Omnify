from django.urls import path
from .views import FitnessClassList, BookingCreate, BookingListByEmail

urlpatterns = [
    path('classes/', FitnessClassList.as_view(), name='class-list'),
    path('book/', BookingCreate.as_view(), name='book-class'),
    path('bookings/', BookingListByEmail.as_view(), name='booking-list'),
]
