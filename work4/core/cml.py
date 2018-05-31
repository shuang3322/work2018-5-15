#!/usr/bin/env python
# -*- coding:utf-8 -*
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from conf import setting
from core import Logical as op
from core import print_log
from tabulate import tabulate


def command_seve(data_list):
    print(setting.DB_FILE)
    with open(setting.DB_FILE, "w", encoding='UTF-8') as f:
        for item in data_list:
            set = ",".join(item)
            f.write(set)
def command_find(data, codm, index):
    # print(data, codm)
    # print(setting.COLUMNS)
    find_key = codm.split()[1].split(",")
    find_list = []
    if '*' in find_key:
        find_key = setting.COLUMNS
        for key in data.keys():
            find_list.append([key])
            find_list_index = find_list.index([key])
            for list_top in find_key[1:]:
                find_list[find_list_index].append(data.get(key).get(list_top).strip())
        find_list = sorted(find_list, key=lambda student: student[0])
    else:
        for key in data.keys():
            list_data = []
            for name in find_key:
                list_data.append(data.get(key).get(name))
            find_list.append(list_data)
    # print(find_list)
    print(tabulate(headers=find_key, tabular_data=find_list, tablefmt="grid"))


def command_delete(data, codm, index):
    print(data, codm)
    print("command_delete")


def command_add(data, codm, index):
    # print(data, codm, index)
    add_list = []
    codm1 = codm.replace("add", "")
    codm1 = codm1.replace("staff_table", "").strip()
    codm2 = codm1.split(",")
    codm2.insert(0,str(int(index[-1])+1))
    for key in index:
        add_list.append([key])
        add_list_index = add_list.index([key])
        for item in setting.COLUMNS[1:]:
            add_list[add_list_index].append(data.get(key).get(item))
    else:
        add_list[-1][-1] += "\n"
    add_list.append(codm2)
    command_seve(add_list)
    print("command_add")


def command_update(data, codm, index):
    print(data, codm)
    print("command_update")


def command_where(query_clause, data):
    operators = {
        '>': op.op_gt,
        '<': op.op_lt,
        '=': op.op_eq,
        'like': op.op_like,
    }

    for op_key, op_func in operators.items():
        if op_key in query_clause:
            column, val = query_clause.split(op_key)
            matched_data = op_func(column.strip(), val.strip(), data)  # 真正的查询数据去啦
            # print_log(matched_data)
            return matched_data

    else:  # 只有在for执行完成 ，且没有中间被 break的情况 下，才执行
        # 没匹配上任何的条件公式
        print_log.print_log("语法错误:where条件只能支持[>,<,=,like]", 'error')
