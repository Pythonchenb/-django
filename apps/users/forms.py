from captcha.fields import CaptchaField
from django import forms

class LoginForm(forms.Form):
    """定义是否必须存在　"""
    username = forms.CharField(required=True)# required　为必须有的　不能为空
    password = forms.CharField(required=True,min_length=5,max_length=20)


class RegisterForm(forms.Form):
    """注册的时候验证码"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField()

