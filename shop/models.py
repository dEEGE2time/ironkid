from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Out of Stock'), (1, 'In Stock'))
CATEGORY = ((0, 'Tops'), (1, 'Pants'), (3, 'Accessories'), (3, 'Artwork'))

class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    price = models.FloatField()
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.username}"
