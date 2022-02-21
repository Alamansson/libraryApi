from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery.decorators import task


@task(name="send_code_email_task")
def send_activation_code(email, code, status):
    if status == 'register':
        context = {
            'text_detail': 'Спасибо за регистрацию',
            'email': email,
            'domain': 'http://localhost:8000',
            'code': code
        }
        message = f'Нажмите на ссылку для активаций: http://127.0.0.1:8000/api/v1/activate/{email}/{code}'

        send_mail(
            'Активация аккаунта',
            message,
            "alamanov.dev@gmail.com",
            [email],
            # html_message=msg_html,
            fail_silently=False
        )
    elif status == 'forgot_password':
        send_mail(
            'Востановления пароля',
            f"Код активаций: {code}",
            'stackoverflow@admin.com',
            [email],
            fail_silently=True,
        )
