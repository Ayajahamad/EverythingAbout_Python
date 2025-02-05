from ast import Num
import psycopg2
import csv

try:
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres",  # Your database name
        user="postgres",  # Your PostgreSQL username
        password="Postgres@123",  # Your PostgreSQL password
        host="localhost",  # Or your host
        port="5432"  # Default port for PostgreSQL
    )

    # Create a cursor object
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Providers_From_Csv (
            Provider_ID VARCHAR(50),
            Provider_Name VARCHAR(100),
            Email VARCHAR(100),
            Hour_Per_Week FLOAT,
            Start_Date DATE
        );
    """)

    # Open and read the CSV file
    with open(r'C:\Users\ayaj\Downloads\employment_1738747882435.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row if it exists
        next(csv_reader, None)
        cur.execute("TRUNCATE TABLE Providers_From_Csv")
        # Loop through each row and insert into the database
        for row in csv_reader:
            Provider_ID, Provider_Name, Email, Hour_Per_Week, Start_Date = row
            if int(Provider_ID) % 2 == 0 :
                cur.execute(
                    "INSERT INTO Providers_From_Csv (Provider_ID, Provider_Name, Email, Hour_Per_Week, Start_Date) VALUES (%s, %s, %s, %s, %s)",
                    (Provider_ID, Provider_Name, Email, Hour_Per_Week, Start_Date)
                )
                print(Provider_ID)  # Printing the Provider_ID for confirmation

    # Commit the transaction if everything is fine
    conn.commit()
    print("Data inserted successfully!")

except Exception as e:
    # If there is any error, rollback the transaction
    conn.rollback()
    print(f"Error occurred: {e}")

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
