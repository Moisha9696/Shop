from django.urls import path

from search import views

app_name = "search"

urlpatterns = [
    path('', views.search_form_view, name='search_form_view'),
    path('results/', views.search_results, name='search_results'),
]
