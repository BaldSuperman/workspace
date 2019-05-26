import smtplib
from email.mime.text import MIMEText
#1395399436@qq.com 发给2556233499@qq.com
msg = MIMEText("sda dad asd ad")
from_addr = "1395399436@qq.com"
from_pwd = "授权码/我邮箱没开启，太费事"
to_addr = "2556233499@qq.com"
#SMTP服务器地址
smtp_srv = "smtp.qq.com"
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr,[to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)