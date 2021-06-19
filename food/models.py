from django.db import models
import os
import random


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    def __str__(self):
        if not self.parent:
            return f"No parent --> {self.name}"
        else:
            return f"{self.parent} --> {self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


def upload_image_path(instance, filename):
    new_name = random.randint(6666666, 9999999)
    name, ext = Food.get_filename_ext(filename)
    final_name = f'{new_name}{ext}'
    return f'foods/images/{final_name}'


class DataABC(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Food(DataABC):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    composition = models.TextField()
    preview = models.ImageField(upload_to=upload_image_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @staticmethod
    def get_filename_ext(filepath):
        base_name = os.path.basename(filepath)
        name, ext = os.path.splitext(base_name)
        return name, ext

    def __str__(self):
        return f'{self.title} - {self.price}'
