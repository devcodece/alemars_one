from django import forms
from . models import TdtProduct

class TdtProductForm(forms.ModelForm):
    class Meta:
        model = TdtProduct
        fields = [
        'tx_product_name',
        'tx_description',
        'gender',
        #'nm_sale_unit',
        'id_subcategory',
        'id_brand',
        'id_vendor',
        #'color',
        #'size',
        #'img_photo1',
        #'img_photo2',
        #'img_photo3',
        ]
        widgets = {
            'tx_product_name':forms.TextInput(
                attrs={
                    'placeholder':'Product name',
                    'class':'form-control'
                }
            ),
            'tx_description':forms.TextInput(
                attrs={
                    'placeholder':'Description',
                    'class':'form-control'
                }
            ),
            'gender':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'id_subcategory':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'id_brand':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'id_vendor':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            
        }