from django import forms

class Aloqaform(forms.Form):
    telefon_raqami=forms.CharField(max_length=100)
    email=forms.EmailField()
    manzil