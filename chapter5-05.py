import pymysql

conn = pymysql.connect(host='127.0.0.1', port = 3306, user = 'root',
                       passwd = 'wuqili2017', db = 'mysql')
#port = 3306  for window system, 

cur = conn.cursor()
cur.execute('USE scraping')

cur.execute('SELECT * FROM pages WHERE id=1')
print(cur.fetchone())
conn.close()