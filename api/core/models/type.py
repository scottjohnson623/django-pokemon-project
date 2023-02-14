from django.db import models

class TypeManager(models.Manager):
    def create_type(self, name, image_url = None):
        type = self.create(name=name, image_url=image_url)
        return type

class Type(models.Model):
    name = models.CharField(max_length=120)
    image_url = models.CharField(max_length=120, blank=True, null=True)
    objects = TypeManager()

    def __str_(self):
        return self.name