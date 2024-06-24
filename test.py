#토큰을 이용한 접근 test
import requests

url = 'http://127.0.0.1:8000/auth'

token_resonse = requests.post(url, data={'username':'admin', 'password':'admin'})

myToken = token_resonse.json()
token = myToken['token']
header = {'Authorization' : 'Token '+token}

resonse = requests.get('http://127.0.0.1:8000/student/list/', headers=header)
print(resonse.text)
