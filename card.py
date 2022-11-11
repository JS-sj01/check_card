from  mail import NMail
import paramiko
import sys
import datetime
import time
import os
import glob
from git import Repo

with open('/root/card/env_restart41/state','r',encoding='utf-8') as f:
     r = f.read()
     print(r)

b = str(r)


def search():
   f = glob.glob(r'/dev/aicard*')
   #f = glob.glob(r'/root/test/txt*')
   files = print(f)
   num_png = len(f)
   print(num_png)

   c = str(num_png)
   if c == '0':
      if b == '1':
         nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         data = {
            "subject":  "10.10.13.41 card lost " + str(nowTime),
            "content":  "10.10.13.41 card lost.....",
            "receiver": 'xsc@tecorigin.com,tecorigin_ops@tecorigin.com,yanghj@tecorigin.com'
            #"receiver": "tecorigin_ops@tecorigin.com"
         }     
         msg = NMail(username="suj@tecorigin.com", password="bsxiSF8odxR97Vkg")
         msg.send_email(data)
         with open('/root/card/env_restart41/state','w',encoding='utf-8') as f:
             w = f.write('0' + str(nowTime))
         dirfile = os.path.abspath('')
         repo = Repo(dirfile)
         g = repo.git
         g.add("--all")
         g.commit("-am auto update")
         g.push()
         print("Successful push!")

      else:
         with open('/root/card/env_restart41/sta','w',encoding='utf-8') as f:
             w = f.write('2')

   else:
     with open('/root/card/env_restart41/state','w',encoding='utf-8') as f:
        w = f.write('1')

if __name__ =="__main__":
   search()
