from django import forms
from django.forms import ModelForm, Textarea, CharField, TextInput
from latte.models import Restaurant, Category


class CreateProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"style": "width: 505px;"}))
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows':15, 'cols':60, 'style':"width: auto"}))
    price = forms.FloatField(min_value=0, widget=forms.TextInput(attrs={"style": "width: 505px;"}))
    queryset = Category.objects.all()
    category = forms.ModelChoiceField(queryset, empty_label=None)
    file_upload = forms.FileField(
        label=("Upload images"),
        widget=forms.FileInput(attrs={'multiple': '', 'class': 'customfile-input' }),
        required=False
    )

class RestaurantInfoForm(ModelForm):
    name = CharField(label='Restaurant name:', widget=TextInput(attrs={"style": "width: 505px;"}))
    class Meta:
        model = Restaurant
        exclude = ('user',)
        widgets = {
            "description": Textarea(attrs={'rows':15, 'cols':60, 'style':"width: auto"}),
        }
