from django import forms  
from .models import Input, STATES, CURRENCY

class InputForm(forms.ModelForm):  

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget=forms.Select())

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit() '}

    currency = forms.ChoiceField(choices=CURRENCY, required=True,
                                 widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['state', 'address', "currency"]
