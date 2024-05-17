import psycopg2
import os
import sys

#print(os.environ)

print("Argumentos:", sys.argv)
'''
try:
    # Connect to your postgres DB
    conn = psycopg2.connect(
        host= sys.argv[1], #HOST_DB
        port= int(sys.argv[2]),
        database= sys.argv[3],
        user= sys.argv[4],
        password= sys.argv[5]
    )
    #python database.py ${{ env.HOST_DB }} ${{ secrets.HOST_PORT }} ${{ env.DATABASE }} ${{ secrets.USER_PG }} ${{ secrets.PGPASSWORD }}
    #python database.py "host ${{ env.HOST_DB }}" "port ${{ secrets.HOST_PORT }}" "database ${{ env.DATABASE }}" "user ${{ secrets.USER_PG }}" "password ${{ secrets.PGPASSWORD }}"
    #Argumentos: ['database.py', '***', '***', '***']

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

'''
