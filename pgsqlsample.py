import psycopg2

conn = psycopg2.connect("dbname='jA78A5D53B48D32872_foodb' user='jA78A5D53B48D32872' password='PhvTZwaQXK6%'")
cur = conn.cursor();

cur.execute("""insert into T1 (foo) values (10) """)

cur.execute("""select * from T1""")
rows = cur.fetchall()
for row in rows:
  print row[0]


cur.close()
conn.close()
