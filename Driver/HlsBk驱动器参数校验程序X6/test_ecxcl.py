import xlrd  # 导入模块
data = xlrd.open_workbook('ID1BkRightOrder1.xls')
table = data.sheets()[0]
nrows = table.nrows
print(nrows)
