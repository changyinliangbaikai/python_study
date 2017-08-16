#-*- coding: utf8 -*-
import xlrd

def excel_table_byindex(file=u'D:\\testeeReport\\4.xls', colnameindex=0, by_index=0):
    data = xlrd.open_workbook(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    list = []
    d = {}
    for i in range(1, nrows):
        name = table.cell(i, 0).value
        flag = table.cell(i, 8).value
        if flag == u'失败':
            if u'定期理财' not in name and u'我的理财' not in name and u'投顾首页' not in name \
                    and u'证通宝' not in name:
                if d.has_key(name):
                    d[name] = d[name]+1
                else:
                    d[name] = 1
    for key in d.keys():
        print key,':',d[key]

def read_data_from_excel(file_path, text_contained_list,text_uncontained_list,select_flag=True):
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    list = []
    d = {}
    for i in range(1, nrows):
        name = table.cell(i, 0).value
        flag = table.cell(i, 8).value
        if flag == u'失败':
            if select_flag:
                tc_flag = True
                tuc_flag = True
                for text_contained in text_contained_list:
                    tc_flag = tc_flag and text_contained in name
                    if not tc_flag:
                        break
                for text_uncontained in text_uncontained_list:
                    tuc_flag = tuc_flag and text_uncontained not in name
                    if not tuc_flag:
                        break
                if tc_flag and tuc_flag:
                    if d.has_key(name):
                        d[name] = d[name] + 1
                    else:
                        d[name] = 1
            else:
                if d.has_key(name):
                    d[name] = d[name] + 1
                else:
                    d[name] = 1
    for key in d.keys():
        print key,':',d[key]


def create_jianhang_card_number():
    start_str = '6217001370022000'
    out = ''
    for i in range(0, 1000):
        if i < 10 :
            out = start_str + '00' + str(i)
        elif i>=10 and i < 100:
            out = start_str + '0' + str(i)
        else:
            out = start_str + str(i)
        print out

def create_bankofchina_card_number():
    start_str = '6217256100000002'
    out = ''
    for i in range(0, 1000):
        if i < 10 :
            out = start_str + '00' + str(i)
        elif i>=10 and i < 100:
            out = start_str + '0' + str(i)
        else:
            out = start_str + str(i)
        print out

def create_zhaohang_card_number():
    start_str = '6214830200000'
    out = ''
    for i in range(0, 1000):
        if i < 10 :
            out = start_str + '00' + str(i)
        elif i>=10 and i < 100:
            out = start_str + '0' + str(i)
        else:
            out = start_str + str(i)
        print out

def create_person_id(file=u'D:\\script_plugins\\account3.xlsx', colnameindex=0, by_index=0):
    data = xlrd.open_workbook(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    list = []
    d = {}
    for i in range(1, nrows):
        id_value = table.cell(i, 1).value
        if 'X' not in id_value:
            print id_value


def check_data():
    file_path = u'D:\\testeeReport\\0804-2.xls'
    text_contained_list = [u'-搜索-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-基金与理财-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-证通宝-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-投顾首页-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-行情-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-非标-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-理财-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print
    text_contained_list = [u'-理财改版-']
    text_uncontained_list = []
    read_data_from_excel(file_path, text_contained_list, text_uncontained_list)
    print


if __name__ == '__main__':
    check_data()
    #create_zhaohang_card_number()
    #create_card_number()
    #create_person_id()
    #create_bankofchina_card_number()