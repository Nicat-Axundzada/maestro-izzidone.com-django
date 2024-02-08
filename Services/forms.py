from django import forms
from django.forms import inlineformset_factory
from .models import Service, SubService


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'image']


class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['title_en', 'image']


SubServiceFormSet = inlineformset_factory(
    Service,
    SubService,
    form=SubServiceForm,
    extra=1,
    can_delete=False,
)
