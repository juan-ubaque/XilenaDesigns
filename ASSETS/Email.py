import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Settings
from django.conf import settings


class Email:
    def __init__(self, email, password):
        #Datos de la cuenta de correo
        self.email      = settings.EMAIL_HOST_USER
        self.password   = settings.EMAIL_HOST_PASSWORD

    def send_email(self, to,Cc, subject, message, listImage=None, litsName=None):
        
        try:
            
            #Conexion con el servidor
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(self.email, self.password)

            #Creacion del mensaje
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to
            msg['Cc'] = Cc
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'html'))

            #si hay imagen adjunta la convertimos en cid y la adjuntamos
            if listImage != None:

                for image, name in zip(listImage, litsName):

                    msg.attach(self.convert_image_cid(image, name))
                    
            #Envio del mensaje
            server.sendmail(self.email, [to,Cc], msg.as_string())
            server.quit() #Cerramos la conexion

            return True
        except Exception as e:
            print('Error al enviar el correo: '+ str(e))
            return False

    @staticmethod
    def  convert_image_cid(image, name):
        
        with open(image, 'rb') as img_file:
                imagen_adjunta = MIMEImage(img_file.read())
                imagen_adjunta.add_header('Content-ID', f'<{name}>')
                
                return imagen_adjunta


