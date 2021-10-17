import pandas as pd
import xlrd

file = pd.ExcelFile("sales.xlsx")
print(file.sheet_names)
sheet = file.parse('sales')
print(sheet.Date)                       # to see only date column
print(sheet.Amount)                     # to see only amount column
print(sheet.loc[0])                     # to see index number 0 values from the table

print(sheet.loc[0,"Amount"])            # to see index number 0 and Amount value
print(sheet.loc[0,"Invoice"])           # to see index number 0 and index value