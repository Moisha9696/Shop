from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.all_list, name='all'),
    path('shop/', views.all_list, name='product_list'),

]