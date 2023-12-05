import psycopg2

conn = psycopg2.connect(
    host="deproject1.cpaxrao0tqen.ap-southeast-1.rds.amazonaws.com",
    database="postgres",
    user="*********",
    password="*********",
    port = "5432")

cur = conn.cursor()

cur.execute("""CREATE TABLE restaurants_LA(
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
)
""")

file_path = 'C:/Users/username/OneDrive/Desktop/DEProjects/restaurantsLA.csv'

copy_sql = """
COPY restaurants_la FROM stdin WITH CSV HEADER
DELIMITER as ','
"""

try:
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
