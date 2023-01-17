import mysql.connector
from hairstylesconfig import USER, HOST, PASSWORD

class FaceShapeNotFoundError (Exception):
    pass

def __init__(self, dbname, answer):
    self.dbname = dbname
    self.answer = answer

def connect_to_db(dbname):
    connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        auth_plugin = 'mysql_native_password',
        database = dbname)
    return connection

def get_hairstyle_recommendations(answer):
    db_connection = None
    try:
        dbname = "face_shapes"
        db_connection = connect_to_db(dbname)
        cur = db_connection.cursor()
        query = "SELECT hairstyle FROM hairstyles WHERE face_shape = '{}' ORDER BY hairstyle".format(answer)
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except:
        raise FaceShapeNotFoundError
    finally:
        if db_connection:
            db_connection.close()

if __name__ == '__main__':
    get_hairstyle_recommendations(1)

