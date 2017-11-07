from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views import View

from users.forms import LoginForm,RegisterForm
from users.models import UserProfile




class CustomBackend(ModelBackend):
    """自定义验证"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        """自动验证"""
        try:
            user = UserProfile.objects.get(username=username)
            user.check_password(password)
            if user is not None:
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{"register_form":register_form})



class LoginView(View):

    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            dict = request.POST
            user_name = dict.get('username','')
            pass_word = dict.get('password','')
            user = authenticate(user_name = user_name,password=pass_word)
            if user is not None:
                login(request,user)
                return render(request,'index.html')
            else:
                return render(request, 'login.html', {'msg': "用户名或者密码错误"})
        else:
            return render(request,'login.html',{"login_form":login_form})