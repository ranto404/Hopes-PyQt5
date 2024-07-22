import sqlite3
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect("gestion.db")
cu = conn.cursor()
# cu.execute(""" CREATE TABLE comptes(
#            email text,
#            password text
# )""")

# cu.execute(""" CREATE TABLE fiches(
#            num text,
#            date text,
#            nom text,
#            poste text,
#            conge text,
#            evaluation text
# )""")

cu.execute("""CREATE TRIGGER IF NOT EXISTS update_montant_total
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    UPDATE products
    SET montant_total = NEW.quantite * NEW.prix_unitaire
    WHERE nom = NEW.nom;
END;""")

# cu.execute(""" CREATE TABLE clients(
#            nom text,
#            prenom text,
#            adresse text,
#            phone text,
#            cin text
# )""")

def show_message_error(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.critical)
    msg.setText(message)
    msg.setWindowTitle("error")
    msg.exec_()

def base():
    try:
        conn =sqlite3.connect("gestion.db")
        cu = conn.cursor()
        return cu, conn
    except sqlite3.Error as e:
        show_message_error(f"Error : {e}")



conn.commit()
conn.close()

# SQLite3 editor