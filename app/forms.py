from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import CustomUser, SubscribeEmail, RegisterActive

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'portfolio_site', 'profile_pic')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')

class RegisterActiveForm(forms.ModelForm):
    class Meta:
        model = RegisterActive
        fields = ('active_name', 'who_register', 'type',)

        widgets = {
            'active_name': forms.TextInput(attrs={'class': 'form-control'}),
            'who_register': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterActiveForm, self).__init__(*args, **kwargs)

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeEmail
        fields = ('subscribe_email',)

        widgets = {
            'subscribe_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here*'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['subscribe_email'].label = "Subscribe to Our News Letter!"

# class Contactform(forms.Form):
#   name = forms.CharField()
#   email = forms.EmailField(label='E-Mail')
#   category = forms.ChoiceField(choice=[('question', 'Question'), ('other', 'Other')]
#   subject = forms.CharField(required=False)
#   body = forms.CharField(widget=forms.Textarea)
