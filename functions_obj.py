#!c:/Python27/python
print "Content-type: text/html"
print
class Test:
    def __init__(self):
        self.name = "Pavan"
        self.var = 12345676


def function():
    return Test()

t = function()
print(t.name)
print(t.var)