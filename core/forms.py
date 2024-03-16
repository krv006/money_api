from django import forms
from .models import Consumption,Sub_category

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['name', 'info', 'cost', 'sub_category', 'time', 'status']

    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    info = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    cost = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sub_category = forms.ModelChoiceField(queryset=Sub_category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}), required=False)
    status = forms.ChoiceField(choices=Consumption.CONSUPTION_CHOISES_FIELD, widget=forms.Select(attrs={'class': 'form-control'}))