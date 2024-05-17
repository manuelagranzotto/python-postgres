import psycopg2
import os
import sys

try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
        host= sys.argv[1],
        port= int(sys.argv[2]),
        database= sys.argv[3],
        user= sys.argv[4],
        password= sys.argv[5]
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM public.contacts")

    # Retrieve query results
    records = cur.fetchall()

    # print the results
    for row in records:
        print(row)

    # Close de connection

    cur.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Não foi possível conectar ao PostgreSQL {e}")

