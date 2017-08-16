# -*- coding: utf-8 -*-
import xlrd
import MySQLdb


def open_excel(file='C:\\Users\\Administrator\\Desktop\\1.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='C:\\Users\\Administrator\\Desktop\\1.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    list = []
    for i in range(2, nrows):
        print table.cell(i, 0).value, table.cell(i, 1).value
        list.append((table.cell(i, 0).value, table.cell(i, 1).value))
    add_one_task_result(list)


def get_db():
    # db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", db="spider", charset="utf8")
    db = MySQLdb.connect(host="192.168.0.128", user="root", passwd="123456", db="migu_data", charset="utf8")
    # db = MySQLdb.connect(host="123.57.26.246", user="root", passwd="g6s8m3t7s", db="spider", charset="utf8")
    cursor = db.cursor()
    return db, cursor


def add_one_task_result(list):
    sql = "insert into appstore (storeName,storeUrl) values (%s,%s)"
    db, cursor = get_db()
    try:
        cursor.executemany(sql, list)
        db.commit()
    except Exception as e:
        print "exception :", e
        db.rollback()
    db.close()


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file='file.xls', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main():
    tables = excel_table_byindex()

    # tables = excel_table_byname()
    # for row in tables:
    #     print row


if __name__ == "__main__":
    main()
