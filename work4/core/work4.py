#!/usr/bin/python
# _*_ coding:utf-8 _*_
import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from tabulate import tabulate
from conf import setting
DB_FILE = setting.DB_FILE
COLUMNS = setting.DB_FILE



def load_db(db_file):
    """
    加载员工信息表，转字典的格式
    :param db_file:
    :return: data
    """

    data = {}
    with open(db_file,"r",encoding='UTF-8') as f:
        f1 = f.readlines()
        for line in f1:
            staff_id,name,age,phone,dept,enrolled_date  = line.split(",")
            data[staff_id]={}
            data[staff_id]['name'] = name
            data[staff_id]['age'] = age
            data[staff_id]['phone'] = phone
            data[staff_id]['dept'] = dept
            data[staff_id]['enrolled_date'] = enrolled_date.strip()
    return data

def print_log(msg,msg_type='info'):
    if msg_type == 'error':
        print("\033[31;1mError:%s\033[0m"%msg)
    else:
        print("\033[32;1mInfo:%s\033[0m"%msg)

def command_find():
    pass
def command_delete():
    pass
def command_add():
    pass
def command_update():
    pass
def command_where():
    pass
def analysis_sentences(cmd):
    """
    解析语句，并执行
    1.
    :param cmd:
    :return:
    """
    from core import command
    syntax_list = {
        'find': command.command_find,
        'del': command.command_delete,
        'update': command.command_update,
        'add': command.command_add,
    }
    #find name,age from staff_table where age > 22
    if cmd.split()[0] in ('find','add','del','update'):
        print(cmd.split())
        # if 'where' in cmd:
        #     query_clause,where_clause = cmd.split("where")
        #     matched_records = command.command_where(where_clause)
        # else:
        #     matched_records = []
        #     for index,staff_id in enumerate(STAFF_DATA['id']):
        #         record = []
        #         for col in COLUMNS:
        #             record.append(STAFF_DATA[col][index])
        #         matched_records.append(record)
        #     query_clause = cmd
        # cmd_action = cmd.split()[0]
        # if cmd_action in syntax_list:
        #     syntax_list[cmd_action](matched_records,query_clause)

    else:
        print_log("语法错误:\n[find\\add\del\\update] [column1,..] from [staff_table] [where] [column][>,..][condtion]\n",'error')
def main():
    """
    程序主入口
    :return:
    """
    while True:
        cmd = input("[staff db]:").strip()
        if not cmd:continue

        analysis_sentences(cmd)

STAFF_DATA = load_db(DB_FILE)

main()