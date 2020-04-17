from django import forms
from admin_app.models import *


class AdminLoginForm(forms.Form):
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )


class CountryForm(forms.ModelForm):
    country_name = forms.CharField(label='Country Name',
                                   widget=forms.TextInput(
                                       attrs={
                                           "placeholder": "e.g : United Kingdom"
                                       }
                                   )
                                   )
    class Meta:
        model = Country
        fields = ('country_name',)


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'
        exclude = ('state_id',)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        exclude = ('city_id',)


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        exclude = ('region_id',)


class RestoCategoryForm(forms.ModelForm):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'
        exclude = ('resto_id',)