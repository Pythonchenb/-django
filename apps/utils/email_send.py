import string
from random import Random

from MxOnline.settings import EMAIL_FROM
from users.models import EmailVerifyRecord
from django.core.mail import send_mail

#　随机生产字符串
def random(randomlength=8):
    code = ''
    # 26个大小写字母加数字
    chars = string.ascii_letters + str(string.digits)
    length = len(chars) - 1

    for i in range(randomlength):
        code += chars[Random().randint(0, length)]
    return code


def send_register_email(email,send_type='register'):
    email_record = EmailVerifyRecord()
    code = random(16)
    email_record.code = code
    email_record.email= email
    email_record.send_type = send_type
    email_record.save()


    if send_type == 'register':
        email_title='慕学在线网注册激活'
        email_body = '请复制激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status =send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            print('发送成功')

    if send_type == 'forget':

        email_title = '慕学在线网密码重置'
        email_body = '请复制重置你的账号：http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print('发送成功')

