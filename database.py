#import psycopg2
#from config import load_config
import os

print(os.environ['PGPASSWORD'])
print(os.environ['USER_PG'])
print(os.environ['HOST_DB'])
print(os.environ['HOST_EC2'])
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

