from django import forms

from operation.models import UserAsk

# 有了modelForm就不需要这form了
# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2)
#     mobile = forms.CharField(required=True,max_length=11,min_length=11)
#     cource_name = forms.CharField(required=True,max_length=20,min_length=5)
#
class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk # 这是要继承的model
        fields = ['name','mobile','course_name']    #这是字段当然如果你还需要自己添加　你也在class外面可以添加