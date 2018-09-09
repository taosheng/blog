
import urllib
import ssl
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from nocheckin import APP_PASSWORD, APP_USER


user = APP_USER
password = APP_PASSWORD

boss = 'support@talent-service.com'
sender = APP_USER

 
def sendZohoMail(to, target, location):
    session = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    session.login(user, password)
    msg = MIMEMultipart()
    msg['From'] = APP_USER
    msg['To'] =  to
    msg['Subject'] = "今日截圖完成～"
    body = """
    您的 {}  截圖完成
    請至 {} 下載
    感謝您~

    """
    msg.attach(MIMEText(body.format(target, location), 'plain'))
    text = msg.as_string()
    session.sendmail(sender, to , text)
    session.quit()


if __name__ == ''
