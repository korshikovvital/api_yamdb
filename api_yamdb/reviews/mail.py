from email.message import EmailMessage  # для красоты, библиотека стандартная
import smtplib


HOST = 'smtp.mail.ru'
PORT = 587
# не безопасно, но в учебных целях можно
# при необходимости спрячем через getenv
USER = 'practicum.teamwork@mail.ru'
PASSWORD = 'AeBibkgmY5SFdd16SL1E'


def send_letter(addressee, text, username=None):
    """Функция для отправки писем. На вход принимает емайл-адресата и текст
    письма. Поле username не обязательно, для красоты."""
    pattern = (
        "Отправьте на эндпоинт /api/v1/auth/token/ следующий POST-запрос:\n"
    )
    full_text = (
        f'{pattern}{{"username": "{username}", "confirmation_code": "{text}"}}'
    )
    msg = EmailMessage()
    msg.set_content(full_text)
    msg['Subject'] = 'Регистрация на сервисе YAMDB'
    msg['From'] = USER
    msg['To'] = addressee
    # подключаемся к почтовому серверу
    smtp = smtplib.SMTP(HOST, PORT)
    # начинаем шифрование TLS
    smtp.starttls()
    # регистрируемся на сервере
    smtp.ehlo()
    # логинимся
    smtp.login(USER, PASSWORD)
    # отправляем письмо
    smtp.send_message(msg)
    # завершаем соединение
    smtp.quit()
