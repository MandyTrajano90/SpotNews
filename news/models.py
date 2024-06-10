from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name

def validate_content(value):
    if len(value.split(" ")) == 1:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')

class News(models.Model):
    title = models.CharField(max_length=200, null=False, validators=[validate_content])
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    categories = models.ManyToManyField(Category, null=False)


    def __str__(self):
        return self.title