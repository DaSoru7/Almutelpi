import mysql.connector

print("Intentando conectar...")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Admin123",
        database="almutelpi",
        port=3306  # sin comillas, como número
    )
    print("✅ Conexión exitosa:", conn)
except mysql.connector.Error as err:
    print("❌ Error al conectar:", err)
except Exception as e:
    print("❗ Error general:", e)