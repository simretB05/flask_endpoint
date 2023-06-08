import mariadb
import dbcreds

def run_procedure(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except Exception as error:
        print('UNEXPECTED ERROR:', error)
    finally:
        if(cursor != None):
         cursor.close()
    if(conn != None):
         conn.close()
    return results