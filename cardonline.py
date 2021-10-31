import requests

headers = {
    'authority': 'cardonline.vn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'origin': 'https://cardonline.vn',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://cardonline.vn/account/register',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cookie': '_landing_page=%2F; _orig_referrer=; _landing_full_page=https://cardonline.vn/; _landing_type=index; _s=c75167ed-831b-444f-8c86-760fa9abf9d3; _v=b1f7fdd1-beb4-4969-829a-7579cc142355; _origin_reference_site=; _v_new=true; _ga=GA1.2.669600415.1635219739; _gid=GA1.2.1213622093.1635219739; _gat=1; __gads=ID=1efb1bd83f9c34c8-2262071a08cc0041:T=1635219739:RT=1635219739:S=ALNI_MZry3CaYsSj0D_c018xpmRzvAQzxg; _ZB_STATIC_359624_TS=1; _ZB_STATIC_VIEW_THROUGH_WIDGET_357295=357295; _ZB_STATIC_VIEW_THROUGH_WIDGET_359581=359581; _ZB_STATIC_DR_test_cookie=test_cookie',
}

data = {
  'FormType': 'customer_register',
  'utf8': 'true',
  'Token': '03AGdBq2531J_y2LPIV_tQpHnNmvdag3gZfDloObMT9hbwb-MiU8pwftJHcPioFu88gtQ_w8fLGhJaiGk7N33hf6OOWjSrTSTHSb3tzjDdv9PFvz8HCZeJVXyo8rbhASmG7ms60kgcJ9sbSimmZQJf2DTx52KV14FIgTUcv3ThbgkxeNT5lPufQmOcFO0Y-hnXXsNpXotGHvNmhSHUmaDOD98frOYBs8JUrndhZ00TKRO8Xa2_ahC4_-erY15_VMtm8b-ArkD_nv2Rq4DNON_9DKM99vbwBVLvW52EnaHF2Ub46Cd8dgMws84J-4-4K3yywHF_wG5qIg5pLQtCYWYzgtgfMy2OIYOR5HxAyLi8J4mRdIqnt6N29y_p5Upbt_5MAar0Fo_9QDAwU7W9S8tEKdmnp52QksijjB3oeD1wQULqhQXlLSH9ZZ8Co2LMMQZ7bAhADOPar93U9LUV_R8uzc-I13fYUEN4IA',
  'firstName': 'Huy B\u1EA3o',
  'lastName': 'Mai',
  'email': 'maihuybao.contact@gmail.com',
  'password': 'maihuybao'
}

response = requests.post('https://cardonline.vn/account/register', headers=headers, data=data)