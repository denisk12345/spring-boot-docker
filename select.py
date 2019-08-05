import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='db',
    user='user',
    password='password'
)
cur = conn.cursor()
cur.execute("SELECT * FROM test;")
result = cur.fetchone()
print(result)
conn.commit()
cur.close()
conn.close()
