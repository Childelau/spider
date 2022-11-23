import pymysql

db = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='successful',
                    db='maoyandb')

cursor = db.cursor()


#sql语句执行，列表元祖
info_list = [('我不是药神','徐峥','2018-07-05'),('你好,李焕英','贾玲','2021-02-12')]
sql = "insert into filmtab values(%s,%s,%s)" 
cursor.executemany(sql, info_list)

db.commit()


