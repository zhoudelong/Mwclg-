import xlrd

excel  = './开发文档/port.xls'
Readsheet = xlrd.open_workbook(excel, encoding_override='utf-8')
sheetNames = Readsheet.sheet_names()

portdict = {}
sheet1 = Readsheet.sheet_by_name(sheetNames[0])  # 获取第一张表
for i in range(1, sheet1.nrows):
    vul = sheet1.row_values(i)
    portdict[vul[0]] = str(vul[-1]).split('：')[-1].strip()

# print(portdict)
for k,v in portdict.items():
    print(k,v)
