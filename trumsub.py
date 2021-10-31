import requests,random,string,threading
def main():
  headers = {
      'authority': 'trumsub.vn',
      'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
      'accept': '*/*',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'x-requested-with': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'origin': 'https://trumsub.vn',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://trumsub.vn/register.html',
      'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
      'cookie': '',
  }
  while True:
    st = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    data = {
    'repassword': st,
    'username': st,
    'email': f'{st}@gmail.com',
    'password': st
  }

    response = requests.post('https://trumsub.vn/respawn/register.html', headers=headers, data=data)
    try:
      if "success" in response.text:
        out = f"{st}|{st}@gmail.com|{st}"
        open("trumsub.txt","a+").write(f'{out}\n')
        print(out)
      else:
        pass
    except:
      pass
for i in range(10000000):
  new_thread = threading.Thread(target=main, args=()).start()
