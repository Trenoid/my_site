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


def get_all_courses():
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
            "from courses "
        )
        #connection.commit()

        #print(f"{cursor.fetchall()}")
        return cursor.fetchall()

def get_all_resurs():
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
            "from resurs "
        )
        #connection.commit()

        #print(f"{cursor.fetchall()}")
        return cursor.fetchall()

def get_all_blog():
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
            "from blog "
        )
        #connection.commit()

        #print(f"{cursor.fetchall()}")
        return cursor.fetchall()


def get_blog(id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            (" SELECT * FROM blog WHERE id ={}".format(id))
        )
        #connection.commit()
        #print(f"{cursor.fetchone()}")
        return cursor.fetchone()

get_blog(1)

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
