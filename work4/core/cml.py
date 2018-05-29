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


def command_find(data, codm):
    print(data, codm)
    print(setting.COLUMNS)
    find_key = []
    find_key = codm.split()[1].split(",")
    find_list = []
    fubd_dict = {}
    if '*' in find_key:
        print(setting.COLUMNS)
        find_key = setting.COLUMNS
        print(find_key)
        for key in data.keys():
            find_list.append([[find_key[0],key]])
            for list_item in find_list:
                for key,item in data.get(key).items():
                    list_item.append([key,item])
    else:
        for key in data.keys():
            list_data = []
            for name in find_key:
                list_data.append(data.get(key).get(name))
            find_list.append(list_data)
    print(find_list)
    print(tabulate(headers=find_key, tabular_data=find_list))


def command_delete(*args, **kwargs):
    print(args, kwargs)
    print("command_delete")


def command_add(*args, **kwargs):
    print(args, kwargs)
    print("command_add")


def command_update(*args, **kwargs):
    print(args, kwargs)
    print("command_update")


def command_where(query_clause, data, ):
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
