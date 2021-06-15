from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code  # берем у юзера активационный код
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}'  # ссылка которая придет юзеру на поту
    to_email = user.email  # берем у юзера его емаил
    send_mail(
        'Subject here',
        full_link,
        'from@example.com',
        [to_email],
        fail_silently=False,
    )
