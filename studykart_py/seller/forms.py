from django import forms


class add_product1(forms.Form):
    product_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'pname',
    }))
    product_desciption = forms.CharField(max_length=300,widget=forms.Textarea(attrs={
        'class':'md-textarea form-control',
        'id':'pcontent',
        'rows':'3',
    }))


class add_product2(forms.Form):
    product_price = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'price',
    }))
    # product_category = forms.ChoiceField(widget=forms.SelectMultiple(attrs={
    #     'class': 'browser-default cutom-select',
    #     'id': 'price',
    # }))
    product_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'id': 'pimg',
        'aria-describedby': 'pimg',
    }))

class edit_product(forms.Form):
    product_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'pname',
    }))
    product_description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'id': 'pcontent',
        'rows': '3',
    }))
    product_price = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'price',
    }))
    product_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'id': 'pimg',
        'aria-describedby': 'pimg',
    }))