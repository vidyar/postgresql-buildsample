import psycopg2

conn = psycopg2.connect("host='127.0.0.1' dbname='foodb' user='postgres'")
cur = conn.cursor();

cur.execute("""create table T1 (foo int)""")

cur.execute("""insert into T1 (foo) values (10) """)

cur.execute("""select * from T1""")

rows = cur.fetchall()
for row in rows:
  print row[0]


cur.close()
conn.close()
