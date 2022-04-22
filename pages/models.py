from django.db import models

# Create your models here.


class Image_upload(models.Model):
    img_id = models.CharField(max_length=50)
    # image = models.URLField(max_length=200)
    image = models.ImageField(upload_to="uploads/",
                              height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.img_id
