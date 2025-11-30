import os
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Кателории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    website = models.URLField(blank=True, verbose_name='Веб-сайт')
    categories = models.ManyToManyField(
        Category,
        related_name='manufacturers',
        verbose_name='Категории',
        blank=True  # если производитель может быть без категорий
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


def product_image_upload_path(instance, filename):
    """
    Формирует путь: products/<ID категории>/<ID продукта>_<NO>.<расширение>
    Где NO начинается с 0 и увеличивается при замене файла
    """
    if not instance.pk or not instance.category_id:
        return f'products/temp/{filename}'
    
    # Получаем расширение файла
    ext = filename.split('.')[-1].lower()
    
    # Ищем следующий доступный номер
    counter = 0
    while True:
        if counter == 0:
            # Первый файл без номера
            new_filename = f"{instance.id}.{ext}"
        else:
            # Последующие файлы с номером
            new_filename = f"{instance.id}_{counter}.{ext}"
        
        new_path = f'products/{instance.category.id}/{new_filename}'
        
        # Проверяем, существует ли файл с таким путем
        if not instance.image or not instance.image.name == new_path:
            if not instance.image.storage.exists(new_path):
                return new_path
        
        counter += 1

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Производитель'
    )
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10,  decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to=product_image_upload_path, blank=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"Продукт {self.name}, Цена : {self.price}"

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])


