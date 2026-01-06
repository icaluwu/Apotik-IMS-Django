from django import forms
from django.utils import timezone

class ReportDateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=timezone.now().date(), required=True)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=timezone.now().date(), required=True)

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date and end_date > timezone.now().date():
            raise forms.ValidationError("End date cannot be in the future.")
        return end_date
