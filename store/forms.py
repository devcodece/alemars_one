from django import forms
from . models import TdtProduct

class TdtProductForm(forms.ModelForm):
    class Meta:
        model = TdtProduct
        fields = [
        'tx_product_name',
        'tx_description',
        'id_category_person',
        #'nm_sale_unit',
        'id_category',
        'id_subcategory',
        'id_brand',
        'id_vendor',
        'id_color',
        'id_photo',
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

class NewProduct(forms.Form):
    name = forms.CharField(max_length=75)
    description = forms.CharField(max_length=300)
    id_category_person = forms.CharField(max_length=50)
    id_category = forms.CharField(max_length=50)
    id_subcategory = forms.CharField(max_length=50)
    id_brand = forms.CharField(max_length=50)
    id_vendor = forms.CharField(max_length=50)
    id_color = forms.CharField(max_length=50)
    id_photo = forms.CharField(max_length=100)


    sku = forms.CharField(max_length=75)
    id_product = forms.CharField(max_length=75)
    id_product_color = forms.CharField(max_length=50)
    id_size = forms.CharField(max_length=4)
    quantity = forms.CharField(max_length=8)
    price = forms.DecimalField(max_digits=9, decimal_places=2)
