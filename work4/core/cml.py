#!/usr/bin/env python
# -*- coding:utf-8 -*

from core import Logical as op
from core import print_log

def command_find(data,codm):
    print(args, kwargs)
    print("command_find")


def command_delete(*args, **kwargs):
    print(args, kwargs)
    print("command_delete")


def command_add(*args, **kwargs):
    print(args, kwargs)
    print("command_add")


def command_update(*args, **kwargs):
    print(args, kwargs)
    print("command_update")


def command_where(query_clause,data,):
    print(query_clause, data)

    operators =  {
        '>':op.op_gt,
        '<':op.op_lt,
        '=':op.op_eq,
        'like':op.op_like,
    }

    for op_key,op_func in operators.items():
        if op_key in query_clause:
            column,val = query_clause.split(op_key)
            matched_data =op_func(column.strip(),val.strip(),data) #真正的查询数据去啦
            #print_log(matched_data)
            return matched_data

    else: #只有在for执行完成 ，且没有中间被 break的情况 下，才执行
        #没匹配上任何的条件公式
        print_log.print_log("语法错误:where条件只能支持[>,<,=,like]",'error')
