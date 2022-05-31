import sys
import requests
from urllib.parse import quote
from time import sleep

def submit(name, username, email, phone, comment, time=1):

    url = "https://help.instagram.com/ajax/help/contact/submit/page"

    payload = f'jazoest=2928&lsd=AVow-_x2AkA&name={quote(name)}&email={email}&instagram_username={username}&mobile_number={phone}&appeal_reason={comment}&support_form_id=606967319425038&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=%5B%5D&__user=0&__a=1&__dyn=7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo6-&__csr=&__req=1o&__hs=19111.BP%3ADEFAULT.2.0.0.0.&dpr=1&__ccg=GOOD&__rev=1005434099&__s=vwzw0x%3Athko2k%3A5zd74l&__hsi=7092103901735683554-0&__comet_req=0&__spin_r=1005434099&__spin_b=trunk&__spin_t=1651259115'

    headers = {
        'authority': 'help.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=F8AEBA80-F0D4-470D-8E4C-E46D8E6F9527; datr=6zZsYhxEcM_93oWfmD5ewLU8; ig_nrcb=1; mid=Ymw8pwALAAGzqrUzJXbioJc1Ky_p; csrftoken=3Bl75kKNr2qj0MzangmPiXHJVxXpM8HI; dpr=1.25',
        'origin': 'https://help.instagram.com',
        'referer': 'https://help.instagram.com/contact/606967319425038?helpref=page_content',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'x-fb-lsd': 'AVow-_x2AkA'
        }

    try:
        while True:
            response = requests.post(url, headers=headers, data=payload)
            sleep(int(data[5]) * 60 * 60)
    except:pass