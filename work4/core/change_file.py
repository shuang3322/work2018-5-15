from conf import setting


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


def seve_db(data_list):
    print(setting.DB_FILE)
    with open(setting.DB_FILE, "w", encoding='UTF-8') as f:
        for item in data_list:
            set = ",".join(item)
            f.write(set)


def dic_to_list(index, data):
    add_list = []
    print(index)
    for key in index:
        add_list.append([key])
        add_list_index = add_list.index([key])
        for item in setting.COLUMNS[1:]:
            add_list[add_list_index].append(data.get(key).get(item))
    return add_list
