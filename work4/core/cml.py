#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import setting
from core import Logical as op
from core import print_log
from core import change_file
from tabulate import tabulate


def command_find(data, codm, index):

    '''
    :param data:数据（字典）
    :param codm:命令参数
    :param index: 字典排序
    :return:
    '''

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
    print(tabulate(headers=find_key, tabular_data=find_list, tablefmt="grid"))


def command_delete(data, codm, index):
    '''
     :param data:数据（字典）
     :param codm:命令参数
     :param index: 字典排序
     :return:
    '''

    all_data, all_index = change_file.load_db(setting.DB_FILE)
    for data_key in data.keys():
        index.pop(index.index(data_key))
    add_list = []
    for key in index:
        add_list.append([key])
        add_list_index = add_list.index([key])
        for item in setting.COLUMNS[1:]:
            add_list[add_list_index].append(all_data.get(key).get(item))
    change_file.seve_db(add_list)


def command_add(data, codm, index):
    '''
     :param data:数据（字典）
     :param codm:命令参数
     :param index: 字典排序
     :return:
    '''
    add_list = []
    codm1 = codm.replace("add", "")
    codm1 = codm1.replace("staff_table", "").strip()
    codm2 = codm1.split(",")
    codm2.insert(0, str(int(index[-1]) + 1))
    for key in index:
        add_list.append([key])
        add_list_index = add_list.index([key])
        for item in setting.COLUMNS[1:]:
            add_list[add_list_index].append(data.get(key).get(item))
    else:
        add_list[-1][-1] += "\n"
    add_list.append(codm2)
    change_file.seve_db(add_list)


def command_update(data, codm, index):
    '''
        :param data:数据（字典）
        :param codm:命令参数
        :param index: 字典排序
        :return:
    '''

    if 'set' in codm and '=' in codm:
        codm_replace = codm.replace("update staff_table set ", "")
        codm_replace = codm_replace.split('=')
        for key, item in data.items():
            item[codm_replace[0]] = codm_replace[1].strip(" \" ")
        all_data, all_index = change_file.load_db(setting.DB_FILE)
        all_data.update(data)
        all_data_list = change_file.dic_to_list(all_index, all_data)
        change_file.seve_db(all_data_list)

    else:
        # 没匹配上任何的条件公式
        print_log.print_log("语法错误:updata 表格 set 条件 where 筛选条件（where条件只能支持[>,<,=,like]）", 'error')


def command_where(query_clause, data):
    '''
    :param query_clause: 查询内容
    :param data: 全部数据字典
    :return: 返回筛选完成数据
    '''

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
