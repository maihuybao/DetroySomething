import requests,random,string,threading
def main():
  headers = {
    'authority': 'www.googleapis.com',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'content-type': 'application/json',
    'x-client-version': 'Chrome/JsCore/8.6.1/FirebaseCore-web',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://beat.vn',
    'x-client-data': 'CKq1yQEIjbbJAQiltskBCMS2yQEIqZ3KAQi00coBCO/yywEInvnLAQjnhMwBCPqEzAEItoXMAQjLicwBCPuKzAE=',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://beat.vn/',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
}
  while True:
    st = ''.join((random.choice(string.ascii_lowercase) for x in range(20)))
    params = (
    ('key', 'AIzaSyCo8WpOMlC1wnLkDxb4VTG4dQmP_DH7ChA'),
)
    data = '{"email":"'+st+'i@gmail.com","password":"'+st+'","returnSecureToken":true}'
    response = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser', headers=headers, params=params, data=data)
    if "email" in response.text:
      out = f"{st}@gmail.com|{st}"
      open("beat.txt","a+").write(f'{out}\n')
      print(out)
    else:
      print(response.status_code)
for i in range(100000):
  new_thread = threading.Thread(target=main, args=()).start()