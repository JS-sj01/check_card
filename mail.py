import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header, make_header


SMTP_TYPE = "smtp.qiye.aliyun.com"


class NMail:
    def __init__(self, username, password, html=False):
        self.server = smtplib.SMTP(SMTP_TYPE, 25)
        self.server.login(username,password)
        self.username = username
        self.html = html

    def send_email(self, data=None):
        subject = data['subject']
        receiver = data['receiver']
        content = data['content']
        if data.get("attachments"):
            # 存在附件 构建邮件
            message = MIMEMultipart()
            for attach in str(data.get("attachments")).split(','):
                print (attach)
                filename = os.path.basename(attach)
                attachment = MIMEText(open(attach, 'rb').read(), 'base64', 'utf-8')
                attachment['"Content-Type"'] = 'application/octet-stream'
                attachment["Content-Disposition"] = 'attachment; filename="%s"' % make_header(
                    [(filename, 'utf-8')]).encode('utf-8')
                message.attach(attachment)
            message.attach(MIMEText(content, 'plain', 'utf-8'))
        else:
            message = MIMEText(content, 'plain', 'utf-8')

        # 收件人
        message['From'] = Header(self.username, 'utf-8')
        # 收件人
        message['To'] = Header(receiver, 'utf-8')
        # 邮件主题
        message['Subject'] = Header(subject, 'utf-8')

        try:
            self.server.sendmail(self.username, str(receiver).split(','), message.as_string())
            print("邮件发送成功!!!")
            self.server.quit()
        except smtplib.SMTPException as e:
            print(e)
            print("邮件发送失败")


if __name__ == "__main__":

    data = {
        "subject": "sshExeCMD+date( %F )",
        "content": "英文",
        "receiver": "1xxxxx@qq.com"
    }
    msg = NMail(username="suj@xxxxx.com", password="bxxxxx")
    msg.send_email(data)

