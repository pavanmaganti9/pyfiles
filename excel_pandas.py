import pandas as pd
# Load the raw data using the ExcelFile object
data = pd.ExcelFile('python/DS_ae.xlsx')

# First, see the sheetnames available
#print(data.sheet_names)

# Take a peek at the first 10 rows of the first tab
#print(data.parse(sheet_name='ae', skiprows=0).head(10))

#print(pd.read_excel('python/DS_ae.xlsx', index_col=0))


print(pd.read_excel('python/DS_ae.xlsx', index_col=None, header=None))