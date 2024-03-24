import psycopg2
from config import host, password,user,db_name


def get_all_books():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT *"
            "from books "
        )
        #connection.commit()

        #print(f"{cursor.fetchall()}")
        return cursor.fetchall()


get_all_books()

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    get_all_books()

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL",_ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
