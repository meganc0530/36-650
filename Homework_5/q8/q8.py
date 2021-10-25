import psycopg2

def display_table():
    conn = psycopg2.connect(host="localhost", port="5432", user="postgres", 
                        password="ILoveSummer17!",  database="postgres"
                       )
    cur = conn.cursor()
    command = (
        "SELECT * FROM employees LIMIT 10"
    )
    cur.execute(command)
    for row in cur:
        print(row)
    cur.close()
    conn.commit()
    conn.close()

display_table()

