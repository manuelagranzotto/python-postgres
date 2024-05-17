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

    # Close de connection

    cur.close()
    conn.close()

    filename = 'resultados.txt'

    # Save the output on a file
    with open(filename, 'w', encoding='utf-8') as file:
        for line in records:
            file.write('\t'.join(map(str, line)) + '\n')
    print(f"Resultados salvos em '{filename}'")

except psycopg2.Error as e:
    print(f"Não foi possível conectar ao PostgreSQL {e}")

