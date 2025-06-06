import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone

# Create a logger for this module
logger = logging.getLogger(__name__)

class FitnessClassList(APIView):
    def get(self, request):
        try:
            classes = FitnessClass.objects.filter(date_time__gte=timezone.now()).order_by('date_time')
            serializer = FitnessClassSerializer(classes, many=True)
            logger.info(f"Fetched {len(serializer.data)} upcoming fitness classes")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Failed to fetch fitness classes: {e}", exc_info=True)
            return Response({"error": "Failed to fetch fitness classes"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = FitnessClassSerializer(data=request.data)
            if serializer.is_valid():
                fitness_class = serializer.save()
                logger.info(f"Created fitness class: {fitness_class.name} at {fitness_class.date_time}")
                return Response(FitnessClassSerializer(fitness_class).data, status=status.HTTP_201_CREATED)
            logger.warning(f"Fitness class creation failed validation: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Failed to create fitness class: {e}", exc_info=True)
            return Response({"error": "Failed to create fitness class"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookingCreate(APIView):
    def post(self, request):
        try:
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                booking = serializer.save()
                logger.info(f"Booking created for {booking.client_name} in class {booking.fitness_class.name}")
                return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
            logger.warning(f"Booking creation failed validation: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Failed to create booking: {e}", exc_info=True)
            return Response({"error": "Failed to create booking"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookingListByEmail(APIView):
    def get(self, request):
        try:
            email = request.query_params.get('email')
            if not email:
                logger.warning("Booking list requested without providing email")
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            bookings = Booking.objects.filter(client_email=email)
            serializer = BookingSerializer(bookings, many=True)
            logger.info(f"Fetched {len(serializer.data)} bookings for email: {email}")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Failed to fetch bookings: {e}", exc_info=True)
            return Response({"error": "Failed to fetch bookings"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

