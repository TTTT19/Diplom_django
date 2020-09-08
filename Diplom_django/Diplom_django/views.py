from django.shortcuts import render

from articles.models import Article
from products.models import Product


def home_view(request):
    articles = Article.objects.order_by('created')
    products = Product.objects.all()

    context = {
        'articles': articles,
        'products': products,
    }

    return render(request, 'index.html', context)
