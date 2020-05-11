import mysql.connector

# import UI

conn = mysql.connector.connect(
    host="localhost", user="jordan", password="persos", database="test"
)

cursor = conn.cursor()

cursor.execute(
    """ 
    CREATE TABLE IF NOT EXISTS Voitures2 (
        ref int (6) NOT NULL,
        voiture varchar(100) DEFAULT NULL,
        marque varchar(100) DEFAULT NULL,
        annee int(4) DEFAULT NULL,
        PRIMARY KEY(ref));"""
)
# car_name = UI.asking_fields().get()

to_insert = {"ref": 1, "voiture": "familiale", "marque": "Zafira", "annee": 2000}
cursor.execute(
    """INSERT INTO Voitures (ref,voiture,marque,annee) VALUES(%(ref)s, "%(voiture)s", "%(marque)s", "%(annee)s")""",
    """INSERT INTO Voitures2 (ref,voiture,marque,annee) VALUES(f"{to_insert[ref][voiture][marque][annee]}")""",
    to_insert,
)
print(f"{to_insert[voiture]}")
conn.commit()
conn.close()
