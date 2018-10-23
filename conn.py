import  pymysql
conn = pymysql.connect(host = "10.11.101.18",user = "test_smj" , passwd = "test_smj" , db = "test_smj")
cur = conn.cursor()
cur.execute("USE test_smj")


cur.execute("INSERT INTO namelist(id,name,title,content) VALUES (128,'a','s','f')")




cur.execute("SELECT * FROM namelist")
conn.commit()
print(cur.fetchall())
cur.close()
conn.close()
