#!c:/Python27/python
print "Content-type: text/html"
print
import pandas as pd
excel_file = "Superstore.xls"
store = pd.read_excel(excel_file)
first5 = store.head()
#print store.shape
colum = store.head()
#print colum

#mem = store.info(memory_usage='deep')
#print mem

#print store.loc[9000,:]

print

print store.loc[0:2,:]

print 

print store[store.City=='Los Angeles']
print store[store.City=='Los Angeles'].State
print
print

print store.loc[store.City=='Seattle',:]

print store.loc[store.City=='Seattle','Customer Name']
print 
#all rows and 2 cols
print store.iloc[:,0:5]
print 
#all 30 rows and all cols
print store.iloc[0:30,:]
print 
colval = pd.read_excel(excel_file, index_col='Country')
print colval

print

print colval.ix['Seattle',0]



#for i, j in store.iterrows(): 
#    print i, j
#    print
	
#for column in store:
#    print store[column]

#for key, value in store.iteritems():
#	print key, value[6]

#for i, column in enumerate(store):
    #print i, store[column]

booleans = []
for length in store.Quantity:
	if length >= 4:
		booleans.append(True)
	else:
		booleans.append(False)
		
#print booleans[0:30]

#print len(booleans)

is_long = store.Series(booleans)

print is_long.head()

