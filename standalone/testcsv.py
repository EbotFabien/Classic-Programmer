# Program to extract a particular row value
import xlrd

loc = ("C:/Users/user/Downloads/Base histo missions EDL 2020-08.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)
for i in range(0,10):
    name=sheet.row_values(i+1)
    box=tuple(name)
    #if name[3] == 'BISMUTH & TEBOUL':
        #name[3] = 1
    #25=z
    box1=(box)
    print(name[84])

        
        
        




