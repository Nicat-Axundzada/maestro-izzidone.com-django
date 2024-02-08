from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        upload_to='services_images/', default='default.png')

    def __str__(self):
        return self.title


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='subservices_images/', default='default.png')

    def __str__(self):
        return f"{self.service.title} - {self.title_en}"
