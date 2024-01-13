from django.db import models
# from django.db.models.fields import CharField, ImageField

class TestModel01(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/images')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última modificación")

    def __str__(self):
        return "id: {}, name: {}, description: {}, image: {}, url: {}".format(self.id, self.name, self.description, self.image, self.url)
