from django import forms  
from .models import Input, Counties, STATES, CURRENCY, COUNTIES

class InputForm(forms.ModelForm):  

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget=forms.Select())

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    currency = forms.ChoiceField(choices=CURRENCY, required=True,
                                 widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['state', 'address', "currency"]



class CountiesForm(forms.ModelForm):  

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    county = forms.ChoiceField(choices = COUNTIES, required = True,
                               widget = forms.Select(attrs = attrs))
    class Meta:

        model = Counties
        fields = ['county']
