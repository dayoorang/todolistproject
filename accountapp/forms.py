from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '아이디 입력',
                                                             'class': 'mb-2'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력',
                                                                  'class': 'mb-3' }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 재입력',
                                                                  'class': 'mb-3' }))
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label= '아이디'
        self.fields['password1'].label= '비밀번호'
        self.fields['password2'].label= '비밀번호 확인'

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디',
                                widget=forms.TextInput(attrs={'placeholder': '아이디 입력',
                                                             'class': 'mt-1 mb-2'}))
    password = forms.CharField(label='아이디',
                                widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력',
                                                                  'class': 'mt-1 mb-3'}))
    class Meta:
        model = User
        fields =['username','password']

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].label= '아이디'
    self.fields['password'].label= '비밀번호'