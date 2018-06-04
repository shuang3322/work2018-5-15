#!/usr/bin/python
# _*_ coding:utf-8 _*_
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from tabulate import tabulate
from conf import setting
from core import cml
from core import print_log
from core import change_file

DB_FILE = setting.DB_FILE


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
        if 'where' in cmd:
            query_clause, where_clause = cmd.split("where")
            matched_records = cml.command_where(where_clause, STAFF_DATA)
            # matched_records = STAFF_DATA

        else:
            # pass
            matched_records = STAFF_DATA
            query_clause = cmd
        #     matched_records = []
        #     for index,staff_id in enumerate(STAFF_DATA['id']):
        #         record = []
        #         for col in COLUMNS:
        #             record.append(STAFF_DATA[col][index])
        #         matched_records.append(record)
        #     query_clause = cmd
        matched_index = STAFF_DATA_INDEX
        cmd_action = cmd.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records, query_clause, matched_index)

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
