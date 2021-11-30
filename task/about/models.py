from django.db import models

# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return self.title