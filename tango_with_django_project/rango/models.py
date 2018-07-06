from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    view = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwags):
        self.slug = slugify(self.name)
        super(Category, self).save(*kwags, **kwags)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    class Meta:
        db_table = 'page'

    def __str__(self):
        return self.title


