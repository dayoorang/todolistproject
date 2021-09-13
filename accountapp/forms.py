from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class SignupForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '아이디 입력',
    #                                                          'class': 'mb-2'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력',
    #                                                               'class': 'mb-3' }))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 재입력',
    #
    #                                                               'class': 'mb-3' }))
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['username'].label= '아이디'
        self.fields['password1'].label= '비밀번호'
        self.fields['password2'].label= '비밀번호 확인'

        self.fields['username'].widget.attrs.update({'type':'text','placeholder':'id를 입력하세요'})
        self.fields['password1'].widget.attrs.update({'type':'password','placeholder':'password를 입력하세요'})
        self.fields['password2'].widget.attrs.update({'type':'password','placeholder':'password를 입력하세요'})

class UserLoginForm(AuthenticationForm):
    # username = forms.CharField(label='id',
    #                             widget=forms.TextInput(attrs={'placeholder': '아이디 입력',
    #                                                          'class': 'mt-1 mb-2'}))
    # password = forms.CharField(label='password',
    #                             widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 입력',
    #                                                               'class': 'mt-1 mb-3'}))
    class Meta:
        model = User
        fields =['username','password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

        self.fields['username'].label = 'ID'
        self.fields['password'].label = 'PASSWORD'

        self.fields['username'].widget.attrs.update({'type':'text','placeholder':'id를 입력하세요'})
        self.fields['password'].widget.attrs.update({'type':'password','placeholder':'password를 입력하세요'})