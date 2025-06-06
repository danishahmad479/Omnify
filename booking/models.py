from django.db import models
import pytz
from django.utils import timezone

# Create your models here.

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Convert date_time to UTC assuming it's created in IST
        if self.date_time.tzinfo is None:
            ist = pytz.timezone('Asia/Kolkata')
            self.date_time = ist.localize(self.date_time)
        self.date_time = self.date_time.astimezone(pytz.UTC)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.date_time}"
    

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"