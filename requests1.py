#!c:/Python27/python
print "Content-type: text/html"
print
import requests

r = requests.get('https://xkcd.com/353/') 

#print dir(r)

#print help(r)

#print r.text

r = requests.get('http://imgs.xkcd.com/comics/python.png')

#print r.content

#with open('comic.png','wb') as f:
#	f.write(r.content)

#print r.status_code

#print r.ok

#print r.headers

payload = {'page':2,'count':25}
r = requests.get('https://httpbin.org/get',params=payload)

#print r.text

#print r.url

payload = {'username':'pavan','password':'12345'}
r = requests.post('https://httpbin.org/post',params=payload)

#print r.text

#print r.json()

r_dict = r.json()
#print r_dict['args']

r = requests.get('https://httpbin.org/basic-auth/pavan/12345',auth =('pavan','12345'))

print r.text