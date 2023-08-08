from django.db import models
from django.urls import reverse
from datetime import date

# Use Field.choices to create a Tuple of choices available for a dropdown
READING_STATUS = (("M", "Morning"), ("A", "Afternoon"), ("E", "Evening"))

# Create your models here.
class Comic(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=250)
    writer = models.CharField(max_length=100)
    penciler = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}-{self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})
    
    # add this new method
    def read_for_today(self):
        return self.reading_set.filter(date=date.today()).count() >= len(READING_STATUS)


class Reading(models.Model):
    date = models.DateField('Read date')
    readings = models.CharField(max_length=1, choices=READING_STATUS, default=READING_STATUS[0][0])

    # Set up foreign key
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_readings_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']