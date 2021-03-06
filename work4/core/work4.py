#!/usr/bin/python
# _*_ coding:utf-8 _*_
import os
import sys
import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import setting
from core import cml
from core import print_log
from core import change_file

DB_FILE = setting.DB_FILE


def load_db(db_file):
    """
    加载员工信息表，转字典的格式
    :param db_file:
    :return: data
    """

    data = {}
    data_index_list = []
    with open(db_file, "r", encoding='UTF-8') as f:
        f1 = f.readlines()
        for line in f1:
            staff_id, name, age, phone, dept, enrolled_date = line.split(",")
            data_index_list.append(staff_id)
            data[staff_id] = {}
            data[staff_id]['name'] = name
            data[staff_id]['age'] = age
            data[staff_id]['phone'] = phone
            data[staff_id]['dept'] = dept
            data[staff_id]['enroll_date'] = enrolled_date
    return data, data_index_list


def analysis_sentences(cmd):
    """
    解析语句，并执行
    1.
    :param cmd:
    :return:
    """

    syntax_list = {
        'find': cml.command_find,
        'del': cml.command_delete,
        'update': cml.command_update,
        'add': cml.command_add,
    }
    # find name,age from staff_table where age > 22
    if cmd.split()[0] in ('find', 'add', 'del', 'update'):
        starttime = datetime.datetime.now()
        if 'where' in cmd:
            query_clause, where_clause = cmd.split("where")
            matched_records = cml.command_where(where_clause, STAFF_DATA)
        else:
            matched_records = STAFF_DATA
            query_clause = cmd

        matched_index = STAFF_DATA_INDEX
        cmd_action = cmd.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records, query_clause, matched_index)
        endtime = datetime.datetime.now()
        run_time= endtime - starttime
        print("执行数据 %s 条，执行时间 %s 毫秒" % (len(matched_records),run_time.microseconds))

    else:
        print_log.print_log(
            "语法错误:\n[find\\add\del\\update] [column1,..] from [staff_table] [where] [column][>,..][condtion]\n",
            'error')


def main():
    """
    程序主入口
    :return:
    """
    while True:
        cmd = input("[staff db]:").strip()
        if not cmd: continue
        analysis_sentences(cmd)
        global STAFF_DATA, STAFF_DATA_INDEX
        data, index = change_file.load_db(DB_FILE)
        STAFF_DATA, STAFF_DATA_INDEX = data, index


STAFF_DATA, STAFF_DATA_INDEX = change_file.load_db(DB_FILE)
main()
