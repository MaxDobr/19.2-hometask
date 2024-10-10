from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts

app_name = CatalogConfig.name

app_cat = CatalogConfig.name

urlpatterns = [
    path('', home, name='home')

]


