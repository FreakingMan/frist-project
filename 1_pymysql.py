# 1_pymysql.py





import pymysql
db = pymysql.connect(host='localhost',
                user = 'root',password = '123456',
                database = 'db2',charset = 'utf8')
try:
    cursor = db.cursor()

    sql_insert = 'insert into sheng(s_name) values('湖北省');'
    cursor.execute(sql_insert)

    sql_delete = 'delete from sheng where id = 8;'
    cursor.execute(sql_delete)
    db.commit()
    print('ok')

except Exception as e:  
    db.rollback()
    print('Failed',e)
cursor.close()
db.close()






# db = pymysql.connect(host = 'localhost')
