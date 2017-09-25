import pymysql

conn = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root',
                       passwd = 'wuqili2017', db = 'mysql')
#port = 3306  for window system, 

cur = conn.cursor()
cur.execute('USE scraping')

cur.execute('SELECT * FROM pages WHERE id=2')
print(cur.execute('SELECT * FROM pages WHERE id=2'))    # result:  1, means true
print(cur.fetchone())     # the data with id = 2
conn.close()