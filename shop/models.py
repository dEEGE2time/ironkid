from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_lenght=200, unique=True)
    price = models.IntegerField()
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    bookmarks = models.ManyToManyField(User, related_name='product_bookmark', blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.title # ?
    
    def number_of_bookmarks(self):
        return self.bookmarks.count()

class Comment(models.Model):
    post = models.PostModel(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.username}"
