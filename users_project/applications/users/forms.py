from django import forms

from django.contrib.auth import authenticate

from .models import User


class RegisterUserForm(forms.ModelForm):
    """Form definition for RegisterUser."""

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Sugerimos que sea mayor o igual a 6 caracteres'
            }))

    passwordConfirm = forms.CharField(
        label='Contraseña (Confirmación)',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar contraseña'}))

    class Meta:
        """Meta definition for RegisterUserform."""

        model = User
        fields = ('username', 'email', 'first_name', 'second_name',
                  'first_last_name', 'second_last_name', 'gender')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        passwordConfirm = self.cleaned_data.get('passwordConfirm')

        if password != passwordConfirm:
            self.add_error('passwordConfirm', 'La contraseña no coincide')

        return password


class LoginForm(forms.Form):

    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Los datos del usuario son incorrectos')

        return self.cleaned_data
