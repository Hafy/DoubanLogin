#encoding:utf-8
from urllib import request,parse
import http.cookiejar
import re
import os

url='https://accounts.douban.com/login'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
#创建一个opener 带cookie的opener
cookie=http.cookiejar.CookieJar()
opener=request.build_opener(request.HTTPCookieProcessor(cookie))
#req=request.Request(url,headers=headers)
opener.addheaders=[(key,value) for key,value in headers.items()]
#res=opener.open(req)
#html=res.read().decode('utf-8')
#print(html)
#print(re.findall(r'<input type=\"hidden\" name=\"lt\" value=\"(.+?)\"',html))
#lt=re.findall(r'<input type=\"hidden\" name=\"lt\" value=\"(.+?)\"',html)
#execution=re.findall(r'<input type=\"hidden\" name=\"execution\" value=\"(.+?)\"',html)
form={'form_email':'email','form_password':'password','redir':'https://www.douban.com','remember':'on','login':'登录'}
post_data=parse.urlencode(form).encode('utf-8')
#req=request.Request(url,post_data)
print(post_data)
resp=opener.open(url,post_data)
fd=open('douban.html','wb')
fd.write(resp.read())
result=resp.read().decode('utf-8')
print(resp.headers.values())



