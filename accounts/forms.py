from django import forms
from .models import Account


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = {'name', 'desc', 'address_one', 'address_two', 'city', 'state', 'phone'}
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Company name',
                'class': 'col-md-12 form-control'}),
            'desc': forms.Textarea(attrs={
                'placeholder': 'Enter description',
                'class': 'form-control'}),
            'address_one':  forms.TextInput(attrs={
                'placeholder': 'Enter Primary address',
                'class': 'col-md-12 form-control'}),
            'address_two':  forms.TextInput(attrs={
                'placeholder': 'Enter Secondary address',
                'class': 'col-md-12 form-control'}),
            'city': forms.TextInput(attrs={
                'placeholder': 'City',
                'class': 'col-md-12 form-control'}),
            'state': forms.TextInput(attrs={
                'placeholder': 'State',
                'class': 'col-md-12 form-control'}),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Mobile phone',
                'class': 'col-md-12 form-control'})
        }