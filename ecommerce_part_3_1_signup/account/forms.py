from django import  forms 
from .models import UserBase

class RegisterationForm(forms.ModelForm):    
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')   
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'reuired':'Sory, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)   
    password2 = forms.CharField(label='Repeat passwor', widget=forms.PasswordInput)
    
    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)   
   
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})