import requests

# url = "http://challenges.laptophackingcoffee.org:8888/"

img_source = "http://www.allthingsclipart.com/08/go.away.10.jpg"

for dirr in range(0, 20):
    if dirr < 10:
        url = f"http://www.allthingsclipart.com/0{dirr}"
    else:
        url = f"http://www.allthingsclipart.com/{dirr}"
    r = requests.get(url)
    if r.status_code != 404:
        print(f"directory: {dirr}; status_code: {r.status_code}")
        # print(f"headers: {r.headers['content-type']}; encoding: {r.encoding}")
        print(r.text)


url = "http://www.allthingsclipart.com/08/go.away.10.jpg"
r = requests.get(url)
