from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
from .models import Category, Product, About, Special, Contact


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    special = Special.objects.all()
    contact = Contact.objects.all()
    articles = About.objects.all()
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    if request.method == 'POST':
         # Форма была передана на обработку
        form = ContactForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            form.save()
    else:
        form = ContactForm()
    return render(request,
                  'cafe/product/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'articles': articles,
                   'special': special,
                   'form': form,
                   'contact': contact,
                   })


def menu(request, category_slug='goryachij-kofe'):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'cafe/product/menu.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   })


def about(request):
    articles = About.objects.all()
    return render(request,
                  'cafe/product/about.html',
                  {'articles': articles,
                   })


def contact(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
         # Форма была передана на обработку
        form = ContactForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            form.save()
    else:
        form = ContactForm()
    return render(request,
                  'cafe/product/contact.html',
                  {'contact': contact,
                   'form': form,
                   })


def special(request):
    special = Special.objects.all()
    return render(request,
                  'cafe/product/special.html',
                  {'special': special,
                   })