import sqlite3

# inserer
def insertion(nom,designation,quantite,unite,prix_unitaire):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO products(nom,designation,quantite,unite,prix_unitaire) VALUES (?,?,?,?,?)"
    listes = [nom,designation,quantite,unite,prix_unitaire]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

def insertion_personnel(nom,prenom,date_naiss,adresse,genre,phone,embauche):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO perso(nom,prenom,date_naiss,adresse,genre,phone,date_embauche) VALUES (?,?,?,?,?,?,?)"
    listes = [nom,prenom,date_naiss,adresse,genre,phone,embauche]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

def ajout_perso():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM perso"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data



def insertion_contenir(num,date,nom,paie,montant):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO contenir(num,date,nom,paie,montant) VALUES (?,?,?,?,?)"
    listes = [num,date,nom,paie,montant]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

   

def ajout_contenir():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM contenir"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data


def ajout():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM products"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data
# effacer
# def effacer(nom,prenom,age,date,nation):
    
def insertion_client(nom,prenom,adresse,phone,cin):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO clients(nom,prenom,adresse,phone,cin) VALUES (?,?,?,?,?)"
    listes = [nom,prenom,adresse,phone,cin]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

   

def ajout_client():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM clients"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data


def insertion_poste(nom,salaire,descri):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO poste(nom,salaire,descri) VALUES (?,?,?)"
    listes = [nom,salaire,descri]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

def ajout_poste():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM poste"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data


def insertion_fiche(num,date,nom,poste,conge,evaluation):
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    pers = "INSERT INTO fiches(num,date,nom,poste,conge,evaluation) VALUES (?,?,?,?,?,?)"
    listes = [num,date,nom,poste,conge,evaluation]
    cu.execute(pers,listes)
    
    
    # print(data)
    conn.commit()
    conn.close()

def ajout_fiche():
    conn = sqlite3.connect("gestion.db")
    cu = conn.cursor()
    recup = "SELECT rowid,* FROM fiches"
    cu.execute(recup)
    data=cu.fetchall()
    conn.close()

    return data




# effacer
# def effacer(nom,prenom,age,date,nation):
    