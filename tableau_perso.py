import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QLineEdit, QDateTimeEdit, QComboBox, QTableWidget, QTableWidgetItem, QDateEdit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QIcon, QFont
from fonction import insertion, ajout_perso, insertion_personnel
from base import *
db, connection = base()


class Tableau_perso_ui(QWidget):
    def __init__(self, gestion_personnel):
        super().__init__()
        self.setWindowTitle("Gestion de Commande d'immeuble")
        # self.setStyleSheet("background-color:#012b3c")

        self.resize(1500,1500)
        self.deconnecter = gestion_personnel

        
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


        self.titre_pers = QLabel(self, text="Listes des personnels")
        self.titre_pers.setGeometry(500,50,500,50)
        self.titre_pers.setStyleSheet("font-size:40px;font-style:normal;font-weight:bold;color:#3c1101")

        self.titre_perso = QLabel(self, text="modifier un personnel :")
        self.titre_perso.setGeometry(20,150,500,30)
        self.titre_perso.setStyleSheet("font-size:20px;font-style:normral;font-weight:bold;color:#3c1101")
        self.titre_perso.setVisible(False)

        self.nom_perso =QLabel(self, text="Nom :")
        self.nom_perso.setGeometry(20,200,120,30)
        self.nom_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.nom_perso.setVisible(False)
        self.nom_perso_input = QLineEdit(self)
        self.nom_perso_input.setGeometry(130,200,250,30)
        self.nom_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.nom_perso_input.setVisible(False)

        self.prenom_perso =QLabel(self, text="Prenom :")
        self.prenom_perso.setGeometry(20,250,120,30)
        self.prenom_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.prenom_perso.setVisible(False)
        self.prenom_perso_input = QLineEdit(self)
        self.prenom_perso_input.setGeometry(130,250,250,30)
        self.prenom_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.prenom_perso_input.setVisible(False)

        self.date_naiss =QLabel(self, text="Date de naissance :")
        self.date_naiss.setGeometry(20,300,190,30)
        self.date_naiss.setStyleSheet("font-size:20px;color:#3c1101")
        self.date_naiss.setVisible(False)
        self.date_naiss_input = QLineEdit(self)
        self.date_naiss_input.setGeometry(210,300,160,30)
        self.date_naiss_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.date_naiss_input.setVisible(False)

        self.adress_perso =QLabel(self, text="Adresse :")
        self.adress_perso.setGeometry(20,350,120,30)
        self.adress_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.adress_perso.setVisible(False)
        self.adress_perso_input = QLineEdit(self)
        self.adress_perso_input.setGeometry(130,350,250,30)
        self.adress_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.adress_perso_input.setVisible(False)

        self.genre_perso =QLabel(self, text="Date d'embauche :")
        self.genre_perso.setGeometry(20,400,190,30)
        self.genre_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.genre_perso.setVisible(False)
        self.genre_perso_input = QLineEdit(self)
        self.genre_perso_input.setGeometry(210,400,160,30)
        self.genre_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.genre_perso_input.setVisible(False)

        self.phone_perso =QLabel(self, text="Phone :")
        self.phone_perso.setGeometry(20,450,120,30)
        self.phone_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.phone_perso.setVisible(False)
        self.phone_perso_input = QLineEdit(self)
        self.phone_perso_input.setGeometry(130,450,250,30)
        self.phone_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.phone_perso_input.setVisible(False)

        self.embauche_perso =QLabel(self, text="Poste :")
        self.embauche_perso.setGeometry(20,500,120,30)
        self.embauche_perso.setStyleSheet("font-size:20px;color:#3c1101")
        self.embauche_perso.setVisible(False)
        self.embauche_perso_input = QComboBox(self)
        self.embauche_perso_input.setGeometry(130,500,250,30)
        self.embauche_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:3px")
        self.embauche_perso_input.setVisible(False)

        self.annonce = QLabel(self)
        self.annonce.setGeometry(20,550,400,30)
        self.annonce.setText("Veuillez séléctionner une ligne dans le tableau pour faire l'action :")
        self.annonce.setStyleSheet("fonte-size:40px;color:#3c1101;font-weight:bold;text-decoration: underline")
        

        self.buton_modifier = QPushButton(self)
        self.buton_modifier.setGeometry(20,600,100,30)
        self.buton_modifier.setText("Modifier")
        self.buton_modifier.setCursor(Qt.PointingHandCursor)
        self.buton_modifier.setStyleSheet("background-color:blue;font-size:16px;color:white;border-radius:10px;font-family:arial;font-weight:bold")
        self.buton_modifier.enterEvent = self.ouvre
        self.buton_modifier.leaveEvent = self.ferme
        self.buton_modifier.setEnabled(False)
        self.buton_modifier.clicked.connect(self.Modifier)


        self.bouton_ajout_perso = QPushButton(self, text="ajouter")
        self.bouton_ajout_perso.setGeometry(300,600,100,30)
        self.bouton_ajout_perso.setStyleSheet("QPushButton{font-size: 20px;background-color:green;color:white;border-radius:10px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:20px;background-color:chartreuse;color:#3c1101})")
        self.bouton_ajout_perso.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_perso.clicked.connect(self.ajouter_perso)
        
        self.buton_effacer = QPushButton(self)
        self.buton_effacer.setGeometry(150,600,100,30)
        self.buton_effacer.setText("Effacer")
        self.buton_effacer.setCursor(Qt.PointingHandCursor)
        self.buton_effacer.setStyleSheet("background-color:red;color:white;font-size:16px;border-radius:10px;font-family:arial;font-weight:bold")
        self.buton_effacer.enterEvent = self.ouvrir
        self.buton_effacer.leaveEvent = self.fermer
        self.buton_effacer.setEnabled(False)
        self.buton_effacer.clicked.connect(self.Effacer)

        self.text = QLabel(self, text="selectionner dans le tableau pour effacer")
        self.text.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text.setVisible(False)
        
        self.text1 = QLabel(self, text="selectionner un ligne dans le tableau pour modifier")
        self.text1.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text1.setVisible(False)
        


        self.recherche_input = QLineEdit(self)
        self.recherche_input.setGeometry(500,160,200,30)
        self.recherche_input.setStyleSheet("font-size:20px;border-radius:10px;color:#3c1101;background-color:white;padding:3px")
        self.btn_recherche = QPushButton(self, text="recherche")
        self.btn_recherche.setGeometry(720,160,120,30)
        self.btn_recherche.setStyleSheet("font-size:14px;border-radius:10px;color:#3c1101;background-color:white;padding:3px")
        self.btn_recherche.setIcon(QIcon('./Gestion du personnel/321.ico'))
        self.btn_recherche.setToolTip('rechercher')
        self.btn_recherche.clicked.connect(self.Rechercher)


        self.tableau = QTableWidget(self)
        self.tableau.setGeometry(500,200,800,400)
        self.tableau.verticalHeader().setVisible(False)

        self.tableau.setStyleSheet("""
            QTableWidget {
                background-image: url(./images/image2.jpg);
                color: #012b3c;
                border-radius: 10px
            }
            QTableWidget::item {
                background-color: #8f028f77;
                border-bottom: 2px solid white;
                border-radius: 3px
            }  
            QTableWidget::item:selected {
                background-color: orange
            }
            
            QHeaderView::section {
                background-color: #3c1101;
                color: white;
                font-weight: bold;
                border: 1px solid white;
                border-radius: 5px   
            }
            QScrollBar:horizontal {
                background-color: #8f028f77;
                border: none;                
                height: 15px
            }
            QScrollBar::handle:horizontal {
                background-color: #012b3c;
                border-radius: 7px
            }
        """)

        self.tableau.setColumnCount(8)
        self.tableau.setRowCount(20)
        self.tableau.setHorizontalHeaderLabels([
           "id", "nom","prenom","naissance", "adresse", "phone", "embauche", "poste"
        ])
        self.tableau.setColumnWidth(0,50)
        self.tableau.setColumnWidth(1,100)
        self.tableau.setColumnWidth(2,100)
        self.tableau.setColumnWidth(3,150)
        self.tableau.setColumnWidth(4,100)
        self.tableau.setColumnWidth(5,100)
        self.tableau.setColumnWidth(6,100)
        self.tableau.setColumnWidth(7,100)
        self.tableau.itemClicked.connect(self.Selectionner)
        
        listes=ajout_perso()
        self.tableau.setRowCount(len(listes))
        for row, rowData in enumerate(listes):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)



        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1150, 20, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)


        self.load_poste()

        

    def ajouter_perso(self):
        self.create_account_window = AjoutPersonnel()
        self.create_account_window.show()



        
    def ouvrir(self, event):
        self.text.setVisible(True)
        self.text.move(self.buton_effacer.pos() + QPoint(10, -20))
    def fermer(self, event):
        self.text.setVisible(False)

    def ouvre(self, event):
        self.text1.setVisible(True)
        self.text1.move(self.buton_modifier.pos() + QPoint(10, -20))
    def ferme(self, event):
        self.text1.setVisible(False)


    def Rechercher(self):
        mot= self.recherche_input.text()
        listes=ajout_perso()
        self.tableau.setRowCount(len(listes))
        j=1
        for i in range(len(listes)):
            if mot in listes[i]:
                self.tableau.setRowCount(j)
                for col, value in enumerate(listes[i]):
                    item = QTableWidgetItem(str(value))
                    self.tableau.setItem(j-1,col,item)
                j += 1



    def Selectionner(self,item):
        # db= sqlite3.connect("crud.db")
        self.titre_perso.setVisible(True)
        # self.buton_modifier.setVisible(True)
        # self.buton_effacer.setVisible(True)
        self.nom_perso_input.setVisible(True)
        self.nom_perso.setVisible(True)
        self.adress_perso_input.setVisible(True)
        self.adress_perso.setVisible(True)
        self.prenom_perso_input.setVisible(True)
        self.prenom_perso.setVisible(True)
        self.date_naiss_input.setVisible(True)
        self.date_naiss.setVisible(True)
        self.genre_perso_input.setVisible(True)
        self.genre_perso.setVisible(True)
        self.phone_perso_input.setVisible(True)
        self.phone_perso.setVisible(True)
        self.embauche_perso_input.setVisible(True)
        self.embauche_perso.setVisible(True)
        # self.text.setVisible(True)

        self.buton_effacer.setEnabled(True)
        self.buton_modifier.setEnabled(True)

        row = item.row()
        col = item.column()
        valeur = item.text()
        self.id = self.tableau.item(row,0).text() 

        print(f"{row,col,valeur,id}")        
        modif = "SELECT * FROM perso WHERE rowid = ?"
        data = db.execute(modif, (self.id,))
        resultats = data.fetchall()
        print(resultats)


        # selectionner un ligne pour modifier 
        self.nom_perso_input.setText(str(resultats[0][0]))
        self.prenom_perso_input.setText(str(resultats[0][1]))
        self.date_naiss_input.setText(str(resultats[0][2]))
        self.adress_perso_input.setText(str(resultats[0][3]))
        self.genre_perso_input.setText(str(resultats[0][4]))
        self.phone_perso_input.setText(str(resultats[0][5]))
        self.embauche_perso_input.setCurrentText(str(resultats[0][6]))
    
    def Modifier(self):

         # Vérifier si une ligne est sélectionnée
        selected_row = self.tableau.currentRow()
        if selected_row != -1:
            # Modifier les données de la ligne sélectionnée
            new_data = ["Nouvelle valeur 1", "Nouvelle valeur 2", ...]  # Remplacez ceci par vos nouvelles données
            for col, value in enumerate(new_data):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(selected_row, col, item)
        else:
            # Afficher un message d'erreur si aucune ligne n'est sélectionnée
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une ligne à modifier.")

        global db, connection
        Anarana = self.nom_perso_input.text()
        Fanampiny = self.prenom_perso_input.text()
        naiss = self.date_naiss_input.text()
        toerana = self.adress_perso_input.text()
        sarangany = self.phone_perso_input.text()
        phone = self.genre_perso_input.text()
        nidirana = self.embauche_perso_input.currentText()
        data = [Anarana,Fanampiny,naiss,toerana,sarangany,nidirana,phone]

        # requete pour la modification
        query = "UPDATE perso SET nom =:nom, prenom =:prenom,adresse =:adresse, genre =:genre, phone =:phone, date_embauche =:date_embauche WHERE rowid =:id"

        db.execute(query,{
            "nom" : Anarana,
            "prenom" : Fanampiny,
            "adresse" : toerana,
            "genre" : sarangany,
            "phone" : phone,
            "date_embauche" : nidirana,
            "id" : self.id
        })

        connection.commit()
        # connection.close()
        # self.buton_modifier.setVisible(False)
        # self.close()
        listes = ajout_perso()
        self.tableau.setRowCount(len(listes))
        for row,rowdata in enumerate(listes):
            for col,value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)

        self.titre_perso.setVisible(False)
        self.nom_perso_input.setVisible(False)
        self.nom_perso.setVisible(False)
        self.adress_perso_input.setVisible(False)
        self.adress_perso.setVisible(False)
        self.prenom_perso_input.setVisible(False)
        self.prenom_perso.setVisible(False)
        self.date_naiss_input.setVisible(False)
        self.date_naiss.setVisible(False)
        self.genre_perso_input.setVisible(False)
        self.genre_perso.setVisible(False)
        self.phone_perso_input.setVisible(False)
        self.phone_perso.setVisible(False)
        self.embauche_perso_input.setVisible(False)
        self.embauche_perso.setVisible(False)


    def Effacer(self):

       
        ligne = self.tableau.selectedItems()
        conn = sqlite3.connect("gestion.db")
        cu = conn.cursor()  
        cu.execute("DELETE FROM perso WHERE rowid =:id",{"id":self.id})


        conn.commit()
        conn.close()

        listes = ajout_perso()

        self.tableau.setRowCount(len(listes))
        for row,rowdata in enumerate(listes):
            for col,value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)


        msg_box = QMessageBox()
        msg_box.setWindowTitle('effacer')
        msg_box.setText('personnel effacer !')
        msg_box.setIcon(QMessageBox.Information)

        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: yellow;
                color: green;
                font-weight: bold;
                border: 2px solid white;
                border-radius: 10px;
                font-size: 16px;
            }
            QMessageBox QPushButton {
                background-color: blue;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #03baf1;
            }
        """)

        font = QFont()
        font.setPointSize(16)
        msg_box.setFont(font)

        msg_box.exec_()

        self.nom_perso_input.setVisible(False)
        self.titre_perso.setVisible(False)
        self.nom_perso.setVisible(False)
        self.adress_perso_input.setVisible(False)
        self.adress_perso.setVisible(False)
        self.prenom_perso_input.setVisible(False)
        self.prenom_perso.setVisible(False)
        self.date_naiss_input.setVisible(False)
        self.date_naiss.setVisible(False)
        self.genre_perso_input.setVisible(False)
        self.genre_perso.setVisible(False)
        self.phone_perso_input.setVisible(False)
        self.phone_perso.setVisible(False)
        self.embauche_perso_input.setVisible(False)
        self.embauche_perso.setVisible(False)

        


    def retour_fenetre1(self):
        self.deconnecter.show()    
        self.hide()

    
    def load_poste(self):
        # Connexion à la base de données
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()

        # Récupération des informations sur les produits depuis la table "products"
        cursor.execute("SELECT nom FROM poste")
        postes = cursor.fetchall()

        # Ajout des noms des produits au QComboBox
        for poste in postes:
            self.embauche_perso_input.addItem(poste[0])

        # Fermeture de la connexion à la base de données
        connection.close()


class AjoutPersonnel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter nouveau personnel")
        self.resize(600,600)

        self.image = QLabel(self)
        image = QPixmap("./images/sieze.jpg")
        size = image.scaled(600,600)
        self.image.setPixmap(size)

        self.ajout_perso = QLabel(self, text="ajouter nouveau personnel")
        self.ajout_perso.setGeometry(20,30,500,30)
        self.ajout_perso.setStyleSheet("font-size:30px;font-family:arial;color:#3c1101")

        self.nom_perso =QLabel(self, text="nom :")
        self.nom_perso.setGeometry(60,100,120,30)
        self.nom_perso.setStyleSheet("font-size:20px;color:white")
        self.nom_perso_input = QLineEdit(self)
        self.nom_perso_input.setGeometry(180,100,250,30)
        self.nom_perso_input.setStyleSheet("border-radius:10px;padding:5px")


        self.prenom_perso =QLabel(self, text="prenom :")
        self.prenom_perso.setGeometry(60,150,120,30)
        self.prenom_perso.setStyleSheet("font-size:20px;color:white")
        self.prenom_perso_input = QLineEdit(self)
        self.prenom_perso_input.setGeometry(180,150,250,30)
        self.prenom_perso_input.setStyleSheet("border-radius:10px;padding:5px")


        self.date_naiss_perso =QLabel(self, text="date de naissance :")
        self.date_naiss_perso.setGeometry(60,200,180,30)
        self.date_naiss_perso.setStyleSheet("font-size:20px;color:white")
        self.date_naiss_perso_input = QDateEdit(self)
        self.date_naiss_perso_input.setGeometry(250,200,200,30)
        self.date_naiss_perso_input.setStyleSheet("border-radius:10px;padding:5px")

        self.adresse_perso =QLabel(self, text="adresse :")
        self.adresse_perso.setGeometry(60,250,120,30)
        self.adresse_perso.setStyleSheet("font-size:20px;color:white")
        self.adresse_perso_input = QLineEdit(self)
        self.adresse_perso_input.setGeometry(180,250,250,30)
        self.adresse_perso_input.setStyleSheet("border-radius:10px;padding:5px")

        self.genre_perso_combo =QLabel(self, text="poste :")
        self.genre_perso_combo.setGeometry(60,300,120,30)
        self.genre_perso_combo.setStyleSheet("font-size:20px;color:white")
        self.genre_perso_combo_input = QComboBox(self)
        self.genre_perso_combo_input.setStyleSheet("border-radius:6px")
        self.genre_perso_combo_input.setGeometry(180,300,250,30)

        self.phone_perso =QLabel(self, text="phone :")
        self.phone_perso.setGeometry(60,350,120,30)
        self.phone_perso.setStyleSheet("font-size:20px;color:white")
        self.phone_perso_input = QLineEdit(self)
        self.phone_perso_input.setGeometry(180,350,250,30)
        self.phone_perso_input.setStyleSheet("border-radius:10px;padding:5px")

        self.embauche_perso =QLabel(self, text="embauche :")
        self.embauche_perso.setGeometry(60,400,120,30)
        self.embauche_perso.setStyleSheet("font-size:20px;color:white")
        self.embauche_perso_input = QLineEdit(self)
        self.embauche_perso_input.setGeometry(180,400,250,30)
        self.embauche_perso_input.setStyleSheet("border-radius:10px;padding:5px")

        self.enregistrer = QPushButton(self, text="Enregistrer")
        self.enregistrer.setGeometry(130,500,100,40)
        self.enregistrer.setStyleSheet("color:white;font-size:20px;border-radius:10px;background-color:green")
        self.enregistrer.setCursor(Qt.PointingHandCursor)
        self.enregistrer.setEnabled(False)

        self.load_poste()

        self.nom_perso_input.textChanged.connect(self.checkInputs)
        self.prenom_perso_input.textChanged.connect(self.checkInputs)
        self.date_naiss_perso_input.dateTimeChanged.connect(self.checkInputs)
        self.adresse_perso_input.textChanged.connect(self.checkInputs)
        self.embauche_perso_input.textChanged.connect(self.checkInputs)
        self.genre_perso_combo_input.currentTextChanged.connect(self.checkInputs)
        self.enregistrer.clicked.connect(self.Enregistrer)

    def checkInputs(self):
        # Vérifier si tous les champs d'entrée sont remplis
        if self.nom_perso_input.text() and self.prenom_perso_input.text() and self.date_naiss_perso_input.text() and self.adresse_perso_input.text() and self.embauche_perso_input.text() and self.genre_perso_combo_input.currentText():
            self.enregistrer.setEnabled(True)
            # QMessageBox.warning(self, 'Champs vides', 'Veuillez remplir tous les champs.')
        else:
            self.enregistrer.setEnabled(False)




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
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableau_perso = QDialog()
    ui = Tableau_perso_ui()
    button = QPushButton("Ouvrir la fenêtre enfant", tableau_perso)
    button.clicked.connect(lambda: AjoutPersonnel().exec_())
    tableau_perso.show()
    sys.exit(app.exec_()) 