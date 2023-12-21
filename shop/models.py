from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Out of Stock"), (1, "In Stock"))
SIZES = (("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL"), ("XXL", "XXL"))


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    size = models.CharField(max_length=3, choices=SIZES, default=0)
    price = models.FloatField()
    description = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    image_alt = models.CharField(max_length=100, null=False, blank=False, default="alt")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)