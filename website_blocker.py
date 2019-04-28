import time
from datetime import datetime as dt
host_temp="hosts"
host_paths=r"/etc/hosts"
redirect="127.0.01"
website_list=["www.facebook.com","facebook.com",
"www.gmail.com","gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,22) < dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
        with open(host_paths,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(host_paths,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            pass
        print("fun hours")
    time.sleep(3)
