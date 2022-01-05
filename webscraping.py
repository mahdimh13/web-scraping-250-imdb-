import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.imdb.com/chart/top/")
soup=BeautifulSoup(req.text,'html.parser')
i=1
li=[]
for link in soup.find_all('a'):
    if link.get('title')==None or link.string==None:
        continue
    li2=[]
    li2.append(link.string)
    li2.append(link.get('title'))
    i=i+1
    li.append(li2)
li3=[]
print("1:chart")
print("2:specific rank")
print("0:exit")
a=int(input("which one?   "))
while(True):
    for rate in soup.find_all("strong"):
        li3.append(rate.string)
    if a==1:
        for k in range (250):
            print(k+1,"_",li[k],"rate:",li3[k]   )  
    if a==2:
        num=int(input("enter a num:"))
        print(li[num-1],"rate:",li3[num-1])
    if a==0:
        print("bye!!!")
        break

    print("1:chart")
    print("2:specific rank")
    print("0:exit")
    
    a=int(input("which one?  "))
