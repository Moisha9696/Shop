from django.contrib import admin
from .models import Category, Manufacturer, Product
from django import forms

@admin.register(Category)
class CatogoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    filter_horizontal = ['categories']


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         widgets = {
#             'category': forms.Select(attrs={'class': 'my-custom-select'}),  # кастомный класс
#         }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'manufacturer']
    list_filter = ['category', 'manufacturer']
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ['category', 'manufacturer']
#    form = ProductForm
