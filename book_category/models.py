from django.db import models
from core.models import TimeStampMixin
from django.utils.text import slugify
# Create your models here.
class Category(TimeStampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class SubCategory(TimeStampMixin):
    parent = models.ForeignKey(Category, related_name="subCat", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title