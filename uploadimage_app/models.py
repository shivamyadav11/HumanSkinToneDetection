from django.db import models

# Create your models here.


class Image_data(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return self.title
