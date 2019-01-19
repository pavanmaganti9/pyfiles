#!c:/Python27/python
print "Content-type: text/html"
print
import class_include
from class_include import numberone
print(numberone)
print(class_include.ageofqueen)
class_include.timesfour(34)
#cfpiano = class_include.Piano()
#cfpiano.printdetails()

stu = class_include.student("Pavan",31)
print(stu.full_name)