from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Name'
        self.fields['password'].label = 'Password'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'phone', 'email_address']

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    email_address = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Name'
        self.fields['password'].label = 'Password'
        self.fields['confirm_password'].label = 'Confirm password'
        self.fields['phone'].label = 'Phone number'
        self.fields['first_name'].label = 'First name'
        self.fields['last_name'].label = 'Last name'
        self.fields['email_address'].label = 'Email'

    def clean_email(self):
        email_address = self.cleaned_data['email_address']
        domain = email_address.split('.')[-1]
        if domain in ['ru', 'net']:
            raise forms.ValidationError(f'Регистрация для домена "{domain}" не возможна')
        if User.objects.filter(email=email_address).exists():
            raise forms.ValidationError(f'Данный почтовый адрес уже зарегистрирован в ситеме')
        return email_address

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Имя {username} занято')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data
