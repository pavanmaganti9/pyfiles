import requests
import csv
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Stock_market'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table1 = soup.find('table', attrs={'class': 'wikitable'})

list_of_rows = []
for row in table1.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("import.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Years to December 31, 2012", "Average Annual Return", "Average Compounded Annual Return"])
writer.writerows(list_of_rows)