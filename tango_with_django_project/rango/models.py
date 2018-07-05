from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'category'

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


