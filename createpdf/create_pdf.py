#!c:/Python27/python
print "Content-type: text/html"
print

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image

import csv

data_file = 'work.csv'

def import_data(data_file):
	person_data = csv.reader(open(data_file,"rb"))
	for row in person_data:
		first_name = row[0]
		last_name = row[1]
		platform = row[2]
		company = row[3]
		pdf_file_name = first_name + '_' + company + '.pdf'
		generate_pdf(first_name, last_name, platform, company)
		
def generate_pdf(first_name, last_name, platform, company):
	person_name = last_name + ' ' + first_name
	c = canvas.Canvas(pdf_file_name, pagesize = A4)
	
	#header text
	c.setFont('Arial', 48, leading=None)
	c.drawCentredString(415, 500, "Certify of Work")
	c.setFont('Times New Roman',24, leading=None)
	c.drawCentredString(415, 450, "This is to certify that")
	#person name
	c.setFont('Arial Bold', 34, leading=None)
	c.drawCentredString(415, 395, person_name)
	
	#some content
	c.setFont('Arial', 20, leading=None)
	c.drawCentredString(415,350,"Working in a company")
	#company name
	c.setFont('Arial', 25, leading=None)
	c.drawCentredString(415,350, company)
	#image
	logo = 'flag.jpg'
	c.drawImage(logo,350, 50, width=None, height=None)
	
	#get all the above data and create a pagesize
	c.showPage()
	print 'hello'
	c.save()
	

	
import_data(data_file)	