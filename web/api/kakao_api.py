import requests
import json

code = "VyPLXKKWJZuRsnk04roh2yycldXhzmhCiRMpd7AGVXiE3JkdEclGowtXU9vPB33895aU3wopcJ8AAAF31ERTLQ"
app_key = "002844830aaef71b10290a14eaa18f09"
authorize_url = "https://kauth.kakao.com/oauth/authorize"
url = "https://kauth.kakao.com/oauth/token"
send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
redirect_uri = "https://localhost.com"


def get_authorize_code(client_id=app_key, redirect_uri=redirect_uri):

    response = requests.get(authorize_url + '?client_id={}&redirect_uri={}\
        &response_type=code'.format(client_id, redirect_uri))

    print(response.url)


def get_access_token(app_key=app_key, code=code, url=url):

    data = {
        "grant_type": "authorization_code",
        "client_id": app_key,
        "redirect_uri": "https://localhost.com",
        "code": code
    }
    response = requests.post(url, data=data)

    tokens = response.json()
    print(tokens)

    with open('kakao_code.json', 'w') as fp:
        json.dump(tokens, fp)


# get_access_token()
def message_myself(url=send_url):

    with open("kakao_code.json", 'r') as fp:
        tokens = json.load(fp)

    print(tokens)

    headers = {
        "Authorization": "Bearer " + tokens['refresh_token']
    }

    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": "Hello, world!",
            "link": {
                "web_url": "www.naver.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.content)


message_myself()
# get_access_token()
# get_authorize_code()

# print(tokens)
