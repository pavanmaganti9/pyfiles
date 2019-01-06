#!c:/Python27/python
print "Content-type: text/html"
print
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel('MentorMindWork.xlsx', sheetname='Sheet1')
 
print("Column headings:")
print(df.columns)
#print df

#print "Pavan"