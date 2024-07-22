# from tkinter import filedialog
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel,QPushButton, QLineEdit, QFileDialog, QTableWidgetItem, QComboBox, QDateEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from fonction import insertion_poste, ajout, insertion_personnel
import sys


class Personnel_ui(QWidget):
    def __init__(self, main_app_window):
        super().__init__()
        self.setWindowTitle("Gestion de Commande d'immeuble")
        # self.setStyleSheet("background-color:#012b3c")
        self.resize(1500,1500)
        self.retour = main_app_window

        
        self.imageFont =QLabel(self)
        self.setGeometry(0,0,1500,1500)
        imageFont = QPixmap("./images/image2.jpg")
        size = imageFont.scaled(1500,1500)
        self.imageFont.setPixmap(size)

        
        self.image =QLabel(self)
        self.image.setGeometry(30,30,70,70)
        self.image.setStyleSheet("border:2px solid white;border-radius:10px")
        image = QPixmap("./images/logo.png")
        size = image.scaled(70,70)
        self.image.setPixmap(size)

        
        self.titre = QLabel(self, text=" Gestion de Personnel MeublePlus-MADA")
        self.titre.setStyleSheet("font-family:arial;font-size:35px;font-family:Arial;font-weight: bold;color:#3c1101")
        self.titre.setGeometry(100, 50, 1000, 60)
        self.titre.setAlignment(Qt.AlignCenter)


        self.bouton_ajout_perso = QPushButton(self, text="liste des personnels")
        self.bouton_ajout_perso.setGeometry(400,200,400,50)
        self.bouton_ajout_perso.setStyleSheet("QPushButton{font-size: 16px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_perso.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_perso.clicked.connect(self.ajouter_tableau_perso)
        # self.bouton_ajout_perso.clicked.connect(self.ajouter_perso)


        self.bouton_ajout_post = QPushButton(self, text="liste des postes")
        self.bouton_ajout_post.setGeometry(400,300,400,50)       
        self.bouton_ajout_post.setStyleSheet("QPushButton{font-size: 20px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_post.clicked.connect(self.ajouter_tableau_poste)


        self.bouton_ajout_fiche = QPushButton(self, text="fiche")
        self.bouton_ajout_fiche.setGeometry(400,400,400,50)        
        self.bouton_ajout_fiche.setStyleSheet("QPushButton{font-size: 20px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_fiche.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_fiche.clicked.connect(self.ajouter_fiche)

        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1150, 20, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)

    def ajouter_tableau_perso(self):
        from tableau_perso import Tableau_perso_ui
        self.tableau_perso = Tableau_perso_ui(self)
        self.tableau_perso.show() 
        self.close()

    def ajouter_tableau_poste(self):
        from tableau_poste import Tableau_poste_ui
        self.tableau_poste = Tableau_poste_ui(self)
        self.tableau_poste.show() 
        self.close()

    def ajouter_fiche(self):
        from fiche_perso import Fiche_ui
        self.fiche_perso = Fiche_ui(self)
        self.fiche_perso.show() 
        self.close()


    def retour_fenetre1(self):
        self.retour.show()    
        self.hide()



    def ajouter_poste(self):
        self.create_account_window = AjoutPoste()
        self.create_account_window.show()



    # def ajouter_perso(self):
    #     self.create_account_window = AjoutPersonnel()
    #     self.create_account_window.show()

class AjoutPersonnel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter nouveau personnel")
        self.resize(600,600)

        self.image =QLabel(self)
        self.setGeometry(0,0,600,600)
        image = QPixmap("./images/bureau.jpg")
        size = image.scaled(600,600)
        self.image.setPixmap(size)

        self.ajout_perso = QLabel(self, text="ajouter nouveau personnel")
        self.ajout_perso.setGeometry(20,30,500,30)
        self.ajout_perso.setStyleSheet("font-size:30px;font-family:arial;color:white")

        self.nom_perso =QLabel(self, text="Nom")
        self.nom_perso.setGeometry(20,100,120,30)
        self.nom_perso.setStyleSheet("font-size:20px;color:white")
        self.nom_perso_input = QLineEdit(self)
        self.nom_perso_input.setGeometry(130,100,250,30)
        self.nom_perso_input.setStyleSheet("border-radius:10px")


        self.prenom_perso =QLabel(self, text="prenom")
        self.prenom_perso.setGeometry(20,150,120,30)
        self.prenom_perso.setStyleSheet("font-size:20px;color:white")
        self.prenom_perso_input = QLineEdit(self)
        self.prenom_perso_input.setGeometry(130,150,250,30)
        self.prenom_perso_input.setStyleSheet("border-radius:10px")


        self.date_naiss_perso =QLabel(self, text="date N")
        self.date_naiss_perso.setGeometry(20,200,120,30)
        self.date_naiss_perso.setStyleSheet("font-size:20px;color:white")
        self.date_naiss_perso_input = QDateEdit(self)
        self.date_naiss_perso_input.setGeometry(130,200,250,30)
        self.date_naiss_perso_input.setStyleSheet("border-radius:10px")

        self.adresse_perso =QLabel(self, text="adresse")
        self.adresse_perso.setGeometry(20,250,120,30)
        self.adresse_perso.setStyleSheet("font-size:20px;color:white")
        self.adresse_perso_input = QLineEdit(self)
        self.adresse_perso_input.setGeometry(130,250,250,30)
        self.adresse_perso_input.setStyleSheet("border-radius:10px")

        self.genre_perso_combo =QLabel(self, text="poste")
        self.genre_perso_combo.setGeometry(20,300,120,30)
        self.genre_perso_combo.setStyleSheet("font-size:20px;color:white")
        self.genre_perso_combo_input = QComboBox(self)
        self.genre_perso_combo_input.setGeometry(130,300,250,30)

        self.phone_perso =QLabel(self, text="phone")
        self.phone_perso.setGeometry(20,350,120,30)
        self.phone_perso.setStyleSheet("font-size:20px;color:white")
        self.phone_perso_input = QLineEdit(self)
        self.phone_perso_input.setGeometry(130,350,250,30)
        self.phone_perso_input.setStyleSheet("border-radius:10px")

        self.embauche_perso =QLabel(self, text="embauche")
        self.embauche_perso.setGeometry(20,400,120,30)
        self.embauche_perso.setStyleSheet("font-size:20px;color:white")
        self.embauche_perso_input = QLineEdit(self)
        self.embauche_perso_input.setGeometry(130,400,250,30)
        self.embauche_perso_input.setStyleSheet("border-radius:10px")


        self.enregistrer = QPushButton(self, text="")
        self.enregistrer.setGeometry(130,500,100,40)
        self.enregistrer.setStyleSheet("color:white;font-size:20px;border-radius:10px;background-color:green")
        self.enregistrer.setCursor(Qt.PointingHandCursor)
        self.enregistrer.clicked.connect(self.Enregistrer)

        self.load_poste()

    def load_poste(self):
        # Connexion à la base de données
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()

        # Récupération des informations sur les produits depuis la table "products"
        cursor.execute("SELECT nom FROM poste")
        postes = cursor.fetchall()

        # Ajout des noms des produits au QComboBox
        for poste in postes:
            self.genre_perso_combo_input.addItem(poste[0])

        # Fermeture de la connexion à la base de données
        connection.close()


    def Enregistrer(self):
        nom = self.nom_perso_input.text()
        prenom = self.prenom_perso_input.text()
        date_naiss = self.date_naiss_perso_input.text()
        adresse = self.adresse_perso_input.text()
        phone = self.phone_perso_input.text()
        embauche = self.embauche_perso_input.text()
        genre = self.genre_perso_combo_input.currentText()
        listes = insertion_personnel(nom,prenom,date_naiss,adresse,phone,embauche,genre)

        self.nom_perso_input.clear()
        self.prenom_perso_input.clear()
        self.date_naiss_perso_input.clear()
        self.phone_perso_input.clear()
        self.adresse_perso_input.clear()
        self.embauche_perso_input.clear()
        self.genre_perso_combo_input.clear()
        self.close()
    

    
class AjoutPoste(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter nouveau client")
        self.resize(600,600)

        self.welcome_label = QLabel(self)
        self.welcome_label.setText("GESTION DE COMMANDE IMMEUBLES")
        self.welcome_label.setStyleSheet("font-size:16px;font-family:arial;font-weight: bolder;color:white")
        self.welcome_label.setGeometry(20, 30, 400, 60)
        
        self.image = QLabel(self)
        image = QPixmap("./images/sieze.jpg")
        size = image.scaled(600,600)
        self.image.setPixmap(size)

        self.ajout_post = QLabel(self, text="ajouter nouveau poste")
        self.ajout_post.setGeometry(20,100,500,30)
        self.ajout_post.setStyleSheet("font-size:30px;font-family:arial;color:white")

        self.nom_poste =QLabel(self, text="Titre")
        self.nom_poste.setGeometry(20,150,120,30)
        self.nom_poste.setStyleSheet("font-size:20px;color:white")
        self.nom_poste_input = QLineEdit(self)
        self.nom_poste_input.setGeometry(130,150,250,30)
        self.nom_poste_input.setStyleSheet("border-radius:10px")


        self.salaire_poste =QLabel(self, text="Salaire")
        self.salaire_poste.setGeometry(20,200,120,30)
        self.salaire_poste.setStyleSheet("font-size:20px;color:white")
        self.salaire_poste_input = QLineEdit(self)
        self.salaire_poste_input.setGeometry(130,200,250,30)
        self.salaire_poste_input.setStyleSheet("border-radius:10px")

        self.descri_poste =QLabel(self, text="descri")
        self.descri_poste.setGeometry(20,250,120,30)
        self.descri_poste.setStyleSheet("font-size:20px;color:white")
        self.descri_poste_input = QLineEdit(self)
        self.descri_poste_input.setGeometry(130,250,250,200)
        self.descri_poste_input.setStyleSheet("border-radius:10px")



        self.enregistrer = QPushButton(self, text="Ajouter")
        self.enregistrer.setGeometry(130,500,100,40)
        self.enregistrer.setStyleSheet("color:white;font-size:20px;border-radius:10px;background-color:green")
        self.enregistrer.setCursor(Qt.PointingHandCursor)
        self.enregistrer.clicked.connect(self.Enregistrer)

    def Enregistrer(self):
        nom = self.nom_poste_input.text()
        salaire = self.salaire_poste_input.text()
        descri = self.descri_poste_input.text()
        listes = insertion_poste(nom,salaire,descri)

        self.nom_poste_input.clear()
        self.salaire_poste_input.clear()
        self.descri_poste_input.clear()
        self.close()

    
    # def Parcourir(self):
    #     image = QFileDialog.getOpenFileName(self, "open files", "","All Files(*)")[0]
    #     image =str(image)
    #     self.image_input.setText(image)
    #     print("ok")





if __name__ == "__main":
    app = QApplication(sys.argv)
    commande = Personnel_ui()
    commande.show()
    sys.exit(app.exec_())