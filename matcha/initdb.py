import psycopg2

conn = psycopg2.connect(database="matcha", user="cwagner")
with conn.cursor() as cur:
    cur.execute(open('schema.sql', 'r').read())
conn.commit()
