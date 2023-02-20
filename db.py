import psycopg

from config import *


def create_table():
    with psycopg.connect(f"dbname={DB_NAME} user={USER} password={PASSWORD} host={HOST}") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id serial PRIMARY KEY,
                    full_name varchar(255),
                    birth_date date,
                    sex varchar(255))
                """)
            conn.commit()
    return


def add_user(data):
    with psycopg.connect(f"dbname={DB_NAME} user={USER} password={PASSWORD} host={HOST}") as conn:
        with conn.cursor() as cur:
            for a in range(len(data)):
                cur.execute("INSERT INTO users (full_name, birth_date, sex) VALUES (%s, %s, %s)",
                            (data[a][0], data[a][1], data[a][2], ))
            conn.commit()
    return


def get_unique_user():
    with psycopg.connect(f"dbname={DB_NAME} user={USER} password={PASSWORD} host={HOST}") as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT DISTINCT ON (full_name || birth_date) 
                       full_name, birth_date, sex, date_part('year', age(birth_date)) 
                FROM users
                """)
            return cur.fetchall()


def get_f_users():
    with psycopg.connect(f"dbname={DB_NAME} user={USER} password={PASSWORD} host={HOST}") as conn:
        with conn.cursor() as cur:
            import time
            start = time.time()
            cur.execute("""
                SELECT *
                FROM users
                WHERE sex = 'male' AND LEFT(full_name,1) = 'F'
                """)

            return time.time() - start, cur.fetchall()
