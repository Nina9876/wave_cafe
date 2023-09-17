from django.contrib import admin
from .models import Category, Product, About, Special, Contact, ContactData


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'email']


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
