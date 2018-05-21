#!/usr/bin/python
# _*_ coding:utf-8 _*_

from tabulate import tabulate
import os

DB_FILE = "staff.db"
COLUMNS = ['id','name','age','phone','dept','enrolled_date']
headers_top = ['id','name','age','data','phone','dept']


def load_db(db_file):
    """
    加载员工信息表，并转成指定的格式
    :param db_file:
    :return:
    """
    data = {}
    for i in COLUMNS:
        data[i] = []

    f = open(db_file,"r",encoding='UTF-8')
    for line in f:
        staff_id,name,age,phone,dept,enrolled_date  = line.split(",")
        data['id'].append(staff_id)
        data['name'].append(name)
        data['age'].append(age)
        data['phone'].append(phone)
        data['dept'].append(dept)
        data['enrolled_date'].append(enrolled_date)
    #print_log(data)
    return data

all_data = load_db(DB_FILE)
print(tabulate(all_data,headers=COLUMNS))