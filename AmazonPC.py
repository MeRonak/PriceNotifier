import requests
from bs4 import BeautifulSoup
print("To exit the program enter . in place of URL")
ama = "a-offscreen"
fli = "_30jeq3 _16Jk6d"

while(True):
    ans = input("flipkart or Amazon:")
    if(ans == "flipkart"):
        ufo = fli
    else:
        ufo = ama
    URL = input("Url:")
    if(URL == "."):
        break
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" }
    r  = requests.get(URL, headers=header)
    s = BeautifulSoup(r.content,'html.parser')
    title = s.find(class_ = ufo).get_text()
    print(title[1:])
