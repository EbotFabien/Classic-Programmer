import xlrd
import openpyxl

loc="C:/Users/user/Downloads/Telegram Desktop/Tarifs de base.xlsx"
wb_obj = openpyxl.load_workbook(loc)
sheet=wb_obj.active
A=['F','G','H','I','J','K','L']


for i in A:
    print(sheet[i][29].value,sheet[i][30].value)
