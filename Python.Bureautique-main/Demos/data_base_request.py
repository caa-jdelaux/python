import psycopg2
from psycopg2 import Error

try:
    # Connect to the PostgreSQL database (replace these with your database details)
    connection = psycopg2.connect(
        user="postgres",
        password="pass123",
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )

    # Create a cursor object using the cursor() method
    cursor = connection.cursor()

    # Define your SELECT query
    select_query = "SELECT * FROM public.utilisateurs;"

    # Execute the SELECT query
    cursor.execute(select_query)

    # Fetch all the rows using fetchall() method
    records = cursor.fetchall()

    # Print each row
    for row in records:
        print(row)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

