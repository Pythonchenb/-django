from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.views import View

from operation.models import UserMessage
from utils.email_send import send_register_email
from users.forms import LoginForm,RegisterForm,ForgetForm, ModifyPwdForm
from users.models import UserProfile,EmailVerifyRecord




class CustomBackend(ModelBackend):
    """自定义验证"""
    def authenticate(self, username=None, password=None, **kwargs):
        """自动验证"""
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            user.check_password(password)
            if user is not None:
                return user
        except Exception as e:
            return None



# 用户注册
class RegisterView(View):
    def get(self, request):
        # get 请求的时候，把验证码组件一系列的 HTML render 到 register.html 里
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            # 判断用户是否存在
            if UserProfile.objects.filter(email=user_name):
                return render(request,'register.html',{'msg':'用户已经存在','register_form': register_form})
            pass_word = request.POST.get('password', '')


            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            send_register_email(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


# 验证用户注册后，在邮件里点击注册链接
class ActiveUserView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        print(all_records)
        if all_records:
            for records in all_records:
                email = records.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')



class LoginView(View):

    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            dict = request.POST
            user_name = dict.get('username','')
            pass_word = dict.get('password','')
            user = authenticate(username = user_name,password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': "用户名未激活邮箱"})

            else:

                return render(request, 'login.html', {'msg': "用户名或者密码错误"})
        else:
            return render(request,'login.html',{"login_form":login_form})

class ForgetPwdView(View):
    def get(self,request):
        forget_pwd = ForgetForm()
        return render(request,'forgetpwd.html',{'forget_pwd':forget_pwd})

    def post(self,request):
        """这里一定判断初始化"""
        forget_pwd = ForgetForm(request.POST)
        # 判断是不是合法
        if forget_pwd.is_valid():
            #接收
            dict = request.POST
            email = dict.get('email',"")
            #修改密码的时候再发送一次邮件
            send_register_email(email,'forget')
            return render(request,'send_success.html')
        else:
            return render(request,'forgetpwd.html',{'forget_pwd':forget_pwd})
#　找回密码
class ResetView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        print(all_records)
        if all_records:
            for records in all_records:
                email = records.email # 取出ｅｍａｉｌ
                #如果找到了
                return render(request,'password_reset.html',{'email':email})
            return render(request, 'login.html')

class ModifyPwdView(View):

    def post(self,request):
        #初始化
        reset_from = ModifyPwdForm(request.POST)
        if reset_from.is_valid():
            dict = request.POST
            new_pwd = dict.get('new_pwd','')
            con_pwd = dict.get('con_pwd','')
            email = dict.get('email','')
            if new_pwd != con_pwd:
                return render(request,'password_reset.html',{'email':email,"msg":'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(con_pwd)
            user.save()
            # 修改成功　　返回登陆
            return render(request,'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request,'password_reset.html',{'email':email,"reset_from":reset_from})
