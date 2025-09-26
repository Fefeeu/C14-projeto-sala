import smtplib
import os
from email.message import EmailMessage

try:
    REMETENTE = os.environ['EMAIL_REMETENTE']
    SENHA = os.environ['SENHA_EMAIL'] 
    DESTINATARIO = os.environ['EMAIL_DESTINATARIO']
    SERVIDOR_SMTP = 'smtp.gmail.com'
    PORTA_SMTP = 587
    ASSUNTO = "Email Pipeline"
    CORPO = "Este email está sendo enviado da Pipeline do repositório: 'C14-projeto-sala'"

    msg = EmailMessage()
    msg['Subject'] = ASSUNTO
    msg['From'] = REMETENTE
    msg['To'] = DESTINATARIO
    msg.set_content(CORPO)

    # --- Envio ---
    with smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP) as server:
        server.starttls()
        server.login(REMETENTE, SENHA)
        server.send_message(msg)
    
    print("E-mail de notificação enviado com sucesso!")

except KeyError as e:
    print(f"!!!Erro: A variável de ambiente {e} não foi definida.")
except Exception as e:
    print(f"!!!Falha ao enviar e-mail: {e}")
    print(f"{REMETENTE}\n{SENHA}\n{DESTINATARIO}")
