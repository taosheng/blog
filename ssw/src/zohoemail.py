
import urllib
import ssl
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from nocheckin import APP_PASSWORD, APP_USER


user = APP_USER
password = APP_PASSWORD

recipient = sys.argv[1]
boss = 'support@talent-service.com'
sender = APP_USER

session = smtplib.SMTP_SSL('smtp.zoho.com', 465)
session.login(user, password)
 
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] =  recipient
msg['Subject'] = "今日截圖完成～"
body = """
您今日{}  截圖完成
請至 {} 下載
感謝您~

"""
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
session.sendmail(sender, boss, text)
session.sendmail(sender, recipient, text)
session.quit()

