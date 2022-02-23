
from django.db import models
import uuid

class PasteBinModel(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, max_length=100)
    content = models.TextField()


    def save(self, *args, **kwargs):
        self.id = self.slug or str(uuid.uuid4())
        super(PasteBinModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} : {self.title} : {self.slug}"