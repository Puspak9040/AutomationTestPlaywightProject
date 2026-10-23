import json
import csv
import openpyxl
def read_json_data(file_path):
    data=[]
    file=open(file_path)
    json_data=json.load(file)
    for record in json_data:
        data.append((record["testName"],record["email"],record["password"],record["expected"]))
    return data
def read_csv_data(file_path):
    data=[]
    file=open(file_path,newline='',encoding='utf-8')
    reader=csv.DictReader(file)
    for row in reader:
        data.append((row["testName"],row["email"],row["password"],row["expected"]))

    return data
def read_excel_data(file_path):
    data=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,max_col=2,values_only=True):
        data.append(row)
    return data





