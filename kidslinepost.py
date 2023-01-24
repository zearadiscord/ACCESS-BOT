import requests,random,string

def randomstring(type):
  if type==1:
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(4)]
    return ''.join(randlst)
  if type==2:
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
    return ''.join(randlst) + "@youtube.com"
  if type==3:
    phone = f"0{random.choice(['8','9'])}0-"
    for i in range(2):
      phone += "".join([random.choice(string.digits) for i in range(4)])
      if len(phone) == 8:
        phone += "-"
    randlst = [random.choice(string.digits) for i in range(16)]
    return phone
  if type==4:
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(16)]
    return ''.join(randlst)

data = {"your-name": randomstring(1),"your-email": randomstring(2),"tel-form1": randomstring(3),"your-message": randomstring(4)}

print(requests.post("https://kidsline.tv/contact/#wpcf7-f4-p111-o1",data=data).status_code)
