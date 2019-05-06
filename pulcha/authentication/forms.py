from django import forms
from django.contrib.auth import authenticate
from .models import GalleryUser


class LogInForm(forms.ModelForm):
    class Meta:
        model = GalleryUser
        fields = ['email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('This user does not exists')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(LogInForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = GalleryUser
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'email2',
            'password',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("emails must match")
        email_qs = GalleryUser.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already being used")

        return super(UserRegistrationForm, self).clean(*args, **kwargs)
