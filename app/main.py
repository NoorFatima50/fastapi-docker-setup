from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_db_message():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages LIMIT 1;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0] if row else "No message found"

@app.get("/")
def home():
    message = get_db_message()
    return {"message_from_db": message}
