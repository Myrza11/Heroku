from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', get_category, name='category')
]