from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(max_length=2550)
    author = models.CharField(max_length=50)
    rating = models.IntegerField()
    review = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.IntegerField()
    category = models.CharField(max_length=50)
    number_of_pages = models.IntegerField()
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
