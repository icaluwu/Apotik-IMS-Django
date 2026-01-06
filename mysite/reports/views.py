from django.shortcuts import render
from .forms import ReportDateRangeForm
from inventory.models import Sale, Purchase
from django.db.models import Sum, F

def reports_dashboard(request):
    return render(request, 'reports_dashboard.html')

def sales_report(request):
    form = ReportDateRangeForm(request.POST or None)
    sales = None
    total_revenue = 0
    if request.method == 'POST':
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            sales = Sale.objects.filter(date__range=[start_date, end_date])
            total_revenue = sales.aggregate(total=Sum(F('quantity') * F('medicine__selling_price')))['total'] or 0
    return render(request, 'sales_report.html', {'form': form, 'sales': sales, 'total_revenue': total_revenue})

def purchase_report(request):
    form = ReportDateRangeForm(request.POST or None)
    purchases = None
    total_expenditure = 0
    if request.method == 'POST':
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            purchases = Purchase.objects.filter(date__range=[start_date, end_date])
            total_expenditure = purchases.aggregate(total=Sum(F('quantity') * F('purchase_price')))['total'] or 0
    return render(request, 'purchase_report.html', {'form': form, 'purchases': purchases, 'total_expenditure': total_expenditure})

def profit_loss_report(request):
    form = ReportDateRangeForm(request.POST or None)
    total_revenue = 0
    total_expenditure = 0
    profit_loss = 0
    if request.method == 'POST':
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            sales = Sale.objects.filter(date__range=[start_date, end_date])
            purchases = Purchase.objects.filter(date__range=[start_date, end_date])
            total_revenue = sales.aggregate(total=Sum(F('quantity') * F('medicine__selling_price')))['total'] or 0
            total_expenditure = purchases.aggregate(total=Sum(F('quantity') * F('purchase_price')))['total'] or 0
            profit_loss = total_revenue - total_expenditure
    return render(request, 'profit_loss_report.html', {
        'form': form,
        'total_revenue': total_revenue,
        'total_expenditure': total_expenditure,
        'profit_loss': profit_loss
    })