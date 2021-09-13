from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect

# Create your views here.
from accountapp.forms import SignupForm, UserLoginForm


class LoginFormView(SuccessMessageMixin, LoginView):
    authentication_form = UserLoginForm
    template_name = "accountapp/login_form.html"
    success_message = "로그인 되었습니다."

login = LoginFormView.as_view()

def logout(request):
    messages.success(request, '로그아웃 되었습니다.')
    return logout_then_login(request)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'{user.username}님 가입을 환영합니다 !')
            return redirect('todoapp:list')
    else:
        form = SignupForm()
    return render(request, 'accountapp/signup_form.html', {'form':form})
