numberone = 143

ageofqueen = 88	

#define function
def printhello():
	print("hello")
	
def timesfour(var):
	print(var * 4)
	
#define a class
class Piano:
	def __init__(self):
		self.type = input("What type of language?")
		self.height = input("What is your height? ")
		self.sal = input("What is your salary? ")
		self.age = input("how old are you? ")
		
	def printdetails(self):
		print("This is" + self.type + " Lang"),
		print(self.height , self.sal , self.age)
		

class student:
	def __init__(self,n,a):
		self.full_name = n
		self.age = a
		
	def get_age(self):
		return self.age