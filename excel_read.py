import xlrd 
  
# Give the location of the file 
loc = ("asd.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0)

#print(sheet.cell_value(0, 0))

'''Extract number of rows'''
#print(sheet.nrows) 

'''Extract number of columns'''
#print(sheet.ncols)

'''Extracting all columns name'''
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i))

'''Extract first column'''	
#for i in range(sheet.nrows): 
#    print(sheet.cell_value(i, 0)) 


'''Extract a particular row value'''	
print(sheet.row_values(1))

'''Get all the rows in excel file'''
#for i in range(sheet.nrows): 
#    print(sheet.row_values(i, 0)) 
