from django.contrib import admin
from .models import Category, Medicine, Purchase, Sale

admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(Purchase)
admin.site.register(Sale)