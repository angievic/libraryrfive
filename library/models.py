from django.db import models


def book_image_path(instance, filename):
    # Generate a unique filename for the uploaded image
    unique_filename = f"{instance.pk}_{filename}"
    
    # Return the path where the image should be stored
    return f"book_images/{unique_filename}"

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True,blank=True)
    editor = models.CharField(max_length=255, null=True,blank=True)
    categories = models.ManyToManyField(Category, null=True,blank=True)
    publication_date = models.CharField(max_length=255,null=True,blank=True)
    authors = models.ManyToManyField(Author, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=book_image_path, blank=True, null=True)
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.title
