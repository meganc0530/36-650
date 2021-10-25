import psycopg2

def build_table():
    conn = psycopg2.connect(host="localhost",  port="5432", user="postgres", password="ILoveSummer17!", database="postgres"
                       )
    cur = conn.cursor()
    command = (
        "CREATE TABLE employees (id SERIAL PRIMARY KEY,fname VARCHAR(10),lname VARCHAR(10))"
    )
    cur.execute(command)
    cur.execute("SELECT * FROM employees")
    print(cur.description)
    cur.close()
    conn.commit()
    conn.close()

build_table()
