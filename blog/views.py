from django.shortcuts import render
from .models import *


def index(request):
    content = Content.objects.all()
    categories = Category.objects.all()
    context = {
        'content' : content,
        'title' : 'Список новостей',
        'categories' : categories,
    }

    return render(request, template_name='blog/index.html', context=context)

def get_category(request, category_id):
    content = Content.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'content' : content,
        'categories' : categories,
        'category' : category,
    }

    return render(request, template_name='blog/category.html', context=context)