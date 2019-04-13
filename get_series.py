#!c:/Python27/python
print "Content-type: text/html"
print
import pandas as pd

s = pd.Series([36,23,56,12,54,87,23,98])
print s
print '<br><br>' 
for prime in s:
    print prime,'<br>'
	
print '<br><br>' 	
for idx, val in enumerate(s):
    print(idx, val),'<br>'

print '<br><br>'	
for index in range(len(s)):
    print index, s[index] ,'<br>'
	
print '<br><br>' 

print s.index
print '<br><br>' 
h = ('AA', '2012-02-01', 100, 10.2)
s1 = pd.Series(h)
print s1
s2 = ['AA', '2012-02-01', 100, 10.2]
s3 = pd.Series(s2, index = ['qw','pl','ko','rt'])
print s3
for index in range(len(s3)):
    print index, s3[index] ,'<br>'
print '<br><br>' 
for index in range(len(s3)):
    print index, s3 ,'<br>'
print '<br><br>'	
expected_dates = ['qw', 'rt', 13, 'ko', 11, 'rt', 100]
s4 = pd.Series(s3, index=expected_dates)
print s4

print '<br><br>'
print s4.describe()

print '<br><br>'

excel_file = "Superstore.xls"
store = pd.read_excel(excel_file, index_col=None, encoding='utf-8')

#segment = store[store['segment'] == 'Home Office']
print store.tail()
print len(store)

print '<br><br>'

oid = store['Sales']
print oid.head()
print '<br><br>'

segment = store[store['City'] == 'Orem']
#print segment.head()
#for index in range(len(oid)):
   # print index, oid[index] ,'<br>'
	
name = store['Customer Name'].value_counts()
print name

#for i in range(len(name)):
    #print i, name ,'<br><br>'
	
import matplotlib.pyplot as plt
p = store['Customer Name'].value_counts()
p.plot()
#plt.show()
print '<br><br>'
gby = store[store['Customer Name'] == 'Brosina Hoffman']
gby.groupby(['Order ID','Customer Name']).size().head()

#print gby

print '<br><br>'

sel_val = store[store.columns[2:4]]
df = pd.DataFrame(store)
print len(df)
print df.shape

pdf = pd.DataFrame(store, columns = ['Order ID', 'Customer Name', 'Country', 'State','Product ID'])
print pdf
for i,row in pdf.iterrows():
    print row['Order ID'], row['Product ID'],row['Country'] ,'<br><br>'
#print df[['Order ID','Customer Name']]
#for index,row in df.iterrows():
 #   print index,row['Order ID'],row['Customer Name'],row['Country'],'<br>'