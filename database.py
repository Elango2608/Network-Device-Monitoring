import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        password="Root@123",
        database="network_inventory"
    )
