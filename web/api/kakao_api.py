import requests
import json

code = "rRTF0rkOzMjbgaz3B5z3BYAbEjwg5K_qBo7GLTQWb5GpjsODPPcO-BNcIaHgCsna6qc5IQo9dNkAAAF3z1s79A"
app_key = "1df5d2e5f8634735c25cf4f37d4df7d0"
url = "https://kauth.kakao.com/oauth/token"
send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


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
        "Authorization": "Bearer " + tokens['access_token']
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


# print(tokens)
