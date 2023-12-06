
from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2

def load_data(file_path):
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT", "5432")  
        )

        cur = conn.cursor()

        copy_sql = """
        COPY restaurants_la FROM stdin WITH CSV HEADER
        DELIMITER as ','
        """

        with open(file_path, 'r') as f:
            cur.copy_expert(copy_sql, f)

        conn.commit()
        print("Data loaded successfully")
    except Exception as e:
        conn.rollback()
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    file_path = os.getenv("FILE_PATH")
    load_data(file_path)
