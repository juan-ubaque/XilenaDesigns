from django.conf import settings
from twilio.rest import Client

from email.mime.image import MIMEImage

#Metodo que envia mensaje a el numero indicado 
#Parametros: numero_destino, mensaje


def enviar_mensaje_whatsapp(numero_destino, mensaje):
    account_sid         = 'ACfd9c16a03df34d86c1f2ac38eef95466'
    auth_token          = '07f2070ad30900ac8b94da3ab26882df'
    twilio_phone_number = 'whatsapp:+14155238886'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensaje,
        from_=twilio_phone_number,
        to=f'whatsapp:{numero_destino}'
    )

    return message.sid


def ConvertImageCid(image, name):
    with open(image, 'rb') as img_file:
            imagen_adjunta = MIMEImage(img_file.read())
            imagen_adjunta.add_header('Content-ID', f'<{name}>')
            
            return imagen_adjunta