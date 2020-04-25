import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import *

def send_email(report_file):
    message = MIMEMultipart()
    with open(report_file,'r',encoding='utf-8') as file:
        content=file.read()

    message.attach(MIMEText(content,'html','utf-8')) #邮件的主题内容,为html格式

    message['From']=sender
    message['To']=receiver
    message['Subject']=subject

    with open(report_file,"rb") as file1:
        file2=file1.read()

    att1=MIMEText(file2,'html','utf-8')  #附件的格式是html,内容是report_file的内容

    att1['Content-Type']='application/octet-stream'
    att1['Content-Disposition']='attachment;filename=%s' % report_file
    message.attach(att1)

    try:
        smtp=smtplib.SMTP_SSL(smtp_server,port)
        smtp.login(user,password)
        smtp.sendmail(sender,receiver,message.as_string())
    except smtplib.SMTPException as e:
        logging.error(str(e))

if __name__=="__main__":
    send_email(report_file)