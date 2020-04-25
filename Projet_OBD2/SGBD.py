import mysql.connector
import UI

conn = mysql.connector.connect(
    host="localhost", user="jordan", password="persos", database="test"
)

cursor = conn.cursor()

cursor.execute(
    """ 
    CREATE TABLE IF NOT EXISTS Voitures (
        ref int (6) NOT NULL,
        voiture varchar(100) DEFAULT NULL,
        marque varchar(100) DEFAULT NULL,
        annee int(4) DEFAULT NULL,
        PRIMARY KEY(ref));"""
)
car_name = UI.asking_fields().get()

to_insert = {"ref": 1, "voiture": car_name, "marque": "Zafira", "annee": 2000}
cursor.execute(
    """INSERT INTO Voitures (ref,voiture,marque,annee) VALUES(%(ref)s, "%(voiture)s", "%(marque)s", "%(annee)s")""",
    to_insert,
)

conn.commit()
conn.close()
