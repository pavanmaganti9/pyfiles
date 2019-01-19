#!c:/Python27/python
print "Content-type: text/html"
print

def func():
    d = dict()
    d['str'] = "Pavan.Maganti"
    d['x'] = 50123
    return d

d = func()
print(d)
