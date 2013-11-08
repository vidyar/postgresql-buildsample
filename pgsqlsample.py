import psycopg2

conn = psycopg2.connect("dbname='foodb' user='shippable'")
cur = conn.cursor();

cur.execute("""insert into T1 (foo) values (10) """)

cur.execute("""select * from T1""")
rows = cur.fetchall()
for row in rows:
  print row[0]


cur.close()
conn.close()
