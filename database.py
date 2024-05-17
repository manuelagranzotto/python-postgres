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
#To see a list of all environment variables:
# print(os.environ)

# def get_vendors():
#     """ Retrieve data from the vendors table """
#     config  = load_config()
#     try:
#         with psycopg2.connect(**config) as conn:
#             with conn.cursor() as cur:
#                 cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
#                 print("The number of parts: ", cur.rowcount)
#                 row = cur.fetchone()

#                 while row is not None:
#                     print(row)
#                     row = cur.fetchone()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
'''
