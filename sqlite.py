import sqlite3

conn=sqlite3.connect("test4.db")

sql="create table sales(customer varchar(20),product varchar(20),price float,date date)"
conn.execute(sql)
data=[("rsds","com",2452,"2018-9-3"),
      ("sdd","sdd",5456,"2018-10-8"),
      ("efed","assfs",66446,"2019-5-21")]
sqlInsert="insert into sales values(?,?,?,?)"
conn.executemany(sqlInsert,data)

cursor=conn.execute("select * from sales")
getRows=cursor.fetchall()
row_count=0
for i in getRows:
      print(i)
      row_count+=1
print(row_count)
conn.close()