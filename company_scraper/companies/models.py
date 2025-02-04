from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "company" 

    def __str__(self):
        return self.name
