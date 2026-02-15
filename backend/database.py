import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="product_managementsys",
            user="postgres",
            password="lol",
            port=5432,
            cursor_factory=RealDictCursor,
        )
        return conn
    except Exception as e:
        raise RuntimeError(f"Error connecting to the database: {e}")
    finally:
        print("Database connection attempt completed.")
