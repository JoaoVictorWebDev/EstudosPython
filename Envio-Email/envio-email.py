import smtplib
import email.message
def enviar_email():


    corpo_email =   f"""
    
    <p>Prezados,</p>
    <p>Mensagem Enviada através de robô</p>
    <p>Assinado João </p>
    """
    msg = email.message.Message()
    msg['Subject'] = "João O homem que vendeu o mundo"
    msg['From'] = 'j.brito@estudante.firjan.senai.br'
    msg['To'] = 'brunoarkov@gmail.com'
    password = 'porra2323'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    #login Credentials for sending the email
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso!')
enviar_email()