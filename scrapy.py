import urllib3
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import xlwt 
from xlwt import Workbook 

wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(1, 0, 'ISBT DEHRADUN') 
sheet1.write(2, 0, 'SHASTRADHARA') 
sheet1.write(3, 0, 'CLEMEN TOWN') 
sheet1.write(4, 0, 'RAJPUR ROAD') 
sheet1.write(5, 0, 'CLOCK TOWER') 
sheet1.write(0, 1, 'ISBT DEHRADUN') 
sheet1.write(0, 2, 'SHASTRADHARA') 
sheet1.write(0, 3, 'CLEMEN TOWN') 
sheet1.write(0, 4, 'RAJPUR ROAD') 
sheet1.write(0, 5, 'CLOCK TOWER') 
  
wb.save('xlwt example.xls') 

html = ('https://en.wikipedia.org/wiki/Stephen_Hawking')
content = requests.get(html).content
soup = BeautifulSoup(content,'lxml')
tags = soup.findAll('div',{'class':'toc'})

len(tags)
#print(soup)

tag = soup.find('div',{'class':'toc'})
#print(type(tag))

links = tag.findAll('a')
#print(links)

#for link in links:
    #print(link.text)
     #results = soup.find_all('span', attrs = {'class':'short_desc'})
#print(results)
#print(html)
#print(soup.title)
#print(soup.title.string)
#print(soup.title.text)
#print(soup.p)



body = soup.body
list_of_rows = []
for paragraph in body.find_all('h3'):
	list_of_cells = []
	print(paragraph.text)
	for cell in paragraph.find_all('h2'):
		text = cell.text.replace('&nbsp;', '')
		list_of_cells.append(text)
list_of_rows.append(list_of_cells)
	
list_of_rows = []
for row in body.find_all('h3'):
    list_of_cells = []
    for cell in row.find_all('h2'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

	
outfile = open("import1.csv", "wb")
writer = csv.writer(outfile)
#writer.writerow(["Years to December 31, 2012", "Average Annual Return", "Average Compounded Annual Return"])
writer.writerows(list_of_rows)