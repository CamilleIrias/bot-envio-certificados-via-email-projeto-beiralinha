import smtplib
import os
from email.message import EmailMessage

from Dados import EMAIL_REMETENTE, SENHA_APP, SMTP_PORT, SMTP_SERVER

class SendEmail:
    def __init__(self):
        self.email = EMAIL_REMETENTE
        self.password = SENHA_APP
        
    def enviar_email(self, aluno, mensagem):               
        msg = EmailMessage()
        msg['From'] = self.email
        msg['To'] = ', '.join(aluno.emails)
        msg['Subject'] = 'Certificado(s) - Projeto Beira Linha'
        msg.set_content(mensagem)
        
        for curso in aluno.cursos:
            self.anexar_certificado(msg, curso.caminho)
    
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.login(self.email, self.password)
                smtp.send_message(msg)
        except Exception as e:
            raise 
    
    def anexar_certificado(sel, msg, caminho):
        if not os.path.exists(caminho):
            print(f"Arquivo não encontrado: {caminho}")
            return

        with open(caminho, 'rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='application',
                subtype='pdf',
                filename=os.path.basename(caminho)
            )