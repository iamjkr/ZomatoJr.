from django import forms


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
