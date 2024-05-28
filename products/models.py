from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    vidio = models.FileField(upload_to='vidio/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    dock = models.FileField(upload_to='dock/', blank=True, null=True)


    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.name