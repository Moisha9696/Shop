import logging

from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

logger = logging.getLogger(__name__)

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Количество',
        widget=forms.NumberInput(attrs={
            'class': 'quantity-input',
            'min': '1'
        })
    )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    