#!/usr/bin/env python
# -*- coding:utf-8 -*


def op_gt(column, condtion_val, data):
    print(column, condtion_val, data)
    print(">")
    data_dir = []
    for key, item in data.items:
        if item[column] > condtion_val:
            data_dir[key] = item
    return data_dir


def op_lt(column, condtion_val, data):
    print(column, condtion_val, data)
    print("<")


def op_eq(column, condtion_val, data):
    print(column, condtion_val, data)
    print("=")


def op_like(column, condtion_val, data):
    print(column, condtion_val, data)
    print("like")
