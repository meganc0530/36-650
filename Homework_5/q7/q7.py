import psycopg2

def insert_into_table():
    conn = psycopg2.connect(host="localhost",  port="5432", user="postgres", password="ILoveSummer17!",  database="postgres"
                       )
    cur = conn.cursor()
    command = ('''INSERT INTO employees (id, fname, lname) VALUES (generate_series(1,500), 
    substr(MD5(random()::text), 0, 5), substr(MD5(random()::text), 0, 5))''')
    cur.execute(command)
    cur.execute("SELECT * FROM employees LIMIT 10")
    for row in cur:
        print(row)
    cur.close()
    conn.commit()
    conn.close()

insert_into_table()

# Referenced https://www.w3resource.com/mysql/encryption-and-compression-functions/md5().php to learn how to use MD5
# to generate strings for dummy records
# Cecilia Xia recommended that I try MD5 to help generate the random dummy records