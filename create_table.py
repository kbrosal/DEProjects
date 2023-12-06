from dotenv import load_dotenv
load_dotenv()

import os
import psycopg2

def create_table():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            port=os.environ.get("DB_PORT", "5432")  
        )

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS restaurants_LA(
            restaurants_name VARCHAR,
            phone_number VARCHAR(15),
            street_address VARCHAR(30),
            locality VARCHAR(30),
            website VARCHAR,
            menu_link VARCHAR,
            categories VARCHAR(50),
            sub_categories VARCHAR(50),
            internal_rating FLOAT,
            number_of_reviews INT,
            TA_ratings FLOAT,
            TA_rating_count INT,
            years_in_business VARCHAR(15),
            top_comment VARCHAR                            
        )""")

        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print("Error: ", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    create_table()
