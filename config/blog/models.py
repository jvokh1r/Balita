from django.db import models


# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class ZoneCat(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='media/')
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    zone_cat = models.ForeignKey(ZoneCat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(default=False)
    msg = models.TextField()

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Article)
def voice_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


    
