import urllib.request
with urllib.request.urlopen('https://www.makrocare.com/') as response:
   html = response.read()
   print(html)