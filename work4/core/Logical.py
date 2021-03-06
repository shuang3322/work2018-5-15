#!/usr/bin/env python
# -*- coding:utf-8 -*


def op_gt(column, condtion_val, data):
    '''
    :param column: 筛选字段
    :param condtion_val: 筛选条件
    :param data: 筛选数据
    :return:
    '''
    data_dir = {}
    for key, item in data.items():
        if column == 'id':
            if int(key) > int(condtion_val):
                data_dir[key] = item
        else:
            if int(item.get(column)) > int(condtion_val):
                data_dir[key] = item
    return data_dir


def op_lt(column, condtion_val, data):
    data_dir = {}
    for key, item in data.items():
        if column == 'id':
            if int(key) < int(condtion_val):
                data_dir[key] = item
        else:
            if int(item.get(column)) < int(condtion_val):
                data_dir[key] = item
    return data_dir


def op_eq(column, condtion_val, data):
    data_dir = {}
    condtion_val = condtion_val.strip(' \" ')
    for key, item in data.items():
        if column == 'id':
            if int(key) == int(condtion_val):
                data_dir[key] = item
        else:
            if item.get(column) == condtion_val:
                data_dir[key] = item
    return data_dir


def op_like(column, condtion_val, data):
    data_dir = {}
    condtion_val = condtion_val.strip(' \" ')
    for key, item in data.items():
        if column == 'id':
            if int(key) == int(condtion_val):
                data_dir[key] = item
        else:
            if item.get(column).find(condtion_val) >= 0:
                data_dir[key] = item
    return data_dir
