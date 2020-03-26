import requests
import json

if __name__== '__main__':
    url = 'http://httpbin.org/post'

    args = { 'name': 'ronald', 'curso': 'python', 'level': 'mid', }

    response = requests.post(url, params=args)
    print(response.url)

    if response.status_code == 200:
        print(response.content)



# import requests

# if __name__== '__main__':
#     url = 'http://httpbin.org/get'

#     args = { 'name': 'ronald', 'curso': 'python', 'level': 'mid', }
#     response = requests.get(url, params=args)

#     if response.status_code == 200:
#         content = response.content
#         print(content)
#         # file = open('google.html', 'wb')
#         # file.write(content)
#         # file.close()
