from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preparation = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    shelf_location = models.CharField(max_length=100, blank=True, null=True)
    min_stock = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT, related_name='purchases')
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    expiry_date = models.DateField()
    supplier = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Purchase: {self.medicine.name} - {self.quantity}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.medicine.stock += self.quantity
            self.medicine.save()
        super().save(*args, **kwargs)

class Sale(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT, related_name='sales')
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Sale: {self.medicine.name} - {self.quantity}'

    @property
    def total_price(self):
        return self.quantity * self.medicine.selling_price

    def clean(self):
        if self.medicine.stock < self.quantity:
            raise ValidationError(f'Not enough stock for {self.medicine.name}. Available stock: {self.medicine.stock}')

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.pk:
            self.medicine.stock -= self.quantity
            self.medicine.save()
        super().save(*args, **kwargs)