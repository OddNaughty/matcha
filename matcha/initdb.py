import psycopg2

conn = psycopg2.connect(database="matcha", user="cwagner")
with conn.cursor() as cur:
    cur.execute(open('sql_dumps/schema.sql', 'r').read())
    cur.execute(open('sql_dumps/matcha_public_users.sql').read())
conn.commit()
