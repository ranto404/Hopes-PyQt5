import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QLineEdit, QDateTimeEdit, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QIcon, QFont
from fonction import insertion, ajout_poste, insertion_poste
from base import *
db, connection = base()


class Tableau_poste_ui(QWidget):
    def __init__(self, gestion_personnel):
        super().__init__()
        self.setWindowTitle("Gestion de Personnel d'immeuble")
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


        self.titre_poste = QLabel(self, text="Listes des postes")
        self.titre_poste.setGeometry(500,50,500,50)
        self.titre_poste.setStyleSheet("font-size:40px;font-style:normal;font-weight:bold;color:#3c1101")

        self.titre_poste = QLabel(self, text="modifier un poste :")
        self.titre_poste.setGeometry(20,150,500,30)
        self.titre_poste.setStyleSheet("font-size:20px;font-style:normal;font-weight:bold;color:#3c1101")
        self.titre_poste.setVisible(False)

        self.nom_poste =QLabel(self, text="Nom :")
        self.nom_poste.setGeometry(20,200,120,30)
        self.nom_poste.setStyleSheet("font-size:20px;color:black")
        self.nom_poste.setVisible(False)
        self.nom_poste_input = QLineEdit(self)
        self.nom_poste_input.setGeometry(130,200,250,30)
        self.nom_poste_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")
        self.nom_poste_input.setVisible(False)

        self.salaire_poste =QLabel(self, text="Salaire :")
        self.salaire_poste.setGeometry(20,250,120,30)
        self.salaire_poste.setStyleSheet("font-size:20px;color:black")
        self.salaire_poste.setVisible(False)
        self.salaire_poste_input = QLineEdit(self)
        self.salaire_poste_input.setGeometry(130,250,250,30)
        self.salaire_poste_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")
        self.salaire_poste_input.setVisible(False)

        self.descri_poste =QLabel(self, text="Déscription :")
        self.descri_poste.setGeometry(20,300,120,30)
        self.descri_poste.setStyleSheet("font-size:20px;color:black")
        self.descri_poste.setVisible(False)
        self.descri_poste_input = QLineEdit(self)
        self.descri_poste_input.setGeometry(130,300,250,30)
        self.descri_poste_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")
        self.descri_poste_input.setVisible(False)


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

        self.bouton_ajout_post = QPushButton(self, text="ajouter")
        self.bouton_ajout_post.setGeometry(300,600,100,30)
        self.bouton_ajout_post.setStyleSheet("QPushButton{font-size: 20px;background-color:green;color:white;border-radius:10px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:20px;background-color:chartreuse;color:#3c1101})")
        self.bouton_ajout_post.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_post.clicked.connect(self.ajouter_poste)

        
        self.buton_effacer = QPushButton(self)
        self.buton_effacer.setGeometry(150,600,100,30)
        self.buton_effacer.setText("Effacer")
        self.buton_effacer.setCursor(Qt.PointingHandCursor)
        self.buton_effacer.setStyleSheet("background-color:red;color:white;font-size:16px;border-radius:10px;font-family:arial;font-weight:bold")
        self.buton_effacer.enterEvent = self.ouvrir
        self.buton_effacer.leaveEvent = self.fermer
        self.buton_effacer.setEnabled(False)
        self.buton_effacer.clicked.connect(self.Effacer)
        # self.buton_effacer.setVisible(False)

        self.text = QLabel(self, text="selectionner dans le tableau pour effacer")
        self.text.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text.setVisible(False)
        
        self.text1 = QLabel(self, text="selectionner un ligne dans le tableau pour modifier")
        self.text1.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text1.setVisible(False)

        self.recherche_input = QLineEdit(self)
        self.recherche_input.setGeometry(500,160,200,30)
        self.recherche_input.setStyleSheet("font-size:20px;border-radius:10px;color:#3c1101;background-color:white;padding:3px;padding-left:3px")
        self.btn_recherche = QPushButton(self, text="recherche")
        self.btn_recherche.setGeometry(720,160,120,30)
        self.btn_recherche.setStyleSheet("font-size:14px;border-radius:10px;color:#3c1101;background-color:white;padding:3px")
        self.btn_recherche.setIcon(QIcon('./Gestion du personnel/321.ico'))
        self.btn_recherche.setToolTip('rechercher')
        self.btn_recherche.clicked.connect(self.Rechercher)


        self.tableau = QTableWidget(self)
        self.tableau.setGeometry(600,200,400,400)
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

        self.tableau.setColumnCount(4)
        self.tableau.setRowCount(20)
        self.tableau.setHorizontalHeaderLabels([
           "id", "nom","salaire","description"
        ])
        self.tableau.setColumnWidth(0,50)
        self.tableau.setColumnWidth(1,100)
        self.tableau.setColumnWidth(2,100)
        self.tableau.setColumnWidth(3,150)
        self.tableau.itemClicked.connect(self.Selectionner)
        
        listes=ajout_poste()
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

    def Rechercher(self):
        mot= self.recherche_input.text()
        listes=ajout_poste()
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
        # self.buton_modifier.setVisible(True)
        self.titre_poste.setVisible(True)
        self.buton_effacer.setVisible(True)
        self.nom_poste_input.setVisible(True)
        self.nom_poste.setVisible(True)
        self.salaire_poste.setVisible(True)
        self.salaire_poste_input.setVisible(True)
        self.descri_poste.setVisible(True)
        self.descri_poste_input.setVisible(True)

        self.buton_modifier.setEnabled(True)
        self.buton_effacer.setEnabled(True)
    
        row = item.row()
        col = item.column()
        valeur = item.text()
        self.id = self.tableau.item(row,0).text() 

        print(f"{row,col,valeur,id}")        
        modif = "SELECT * FROM poste WHERE rowid = ?"
        data = db.execute(modif, (self.id,))
        resultats = data.fetchall()
        print(resultats)


        # selectionner un ligne pour modifier 
        self.nom_poste_input.setText(str(resultats[0][0]))
        self.salaire_poste_input.setText(str(resultats[0][1]))
        self.descri_poste_input.setText(str(resultats[0][2]))
    
    def Modifier(self):
        global db, connection
        Anarana = self.nom_poste_input.text()
        karama = self.salaire_poste_input.text()
        mombamomba = self.descri_poste_input.text()
        data = [Anarana,karama,mombamomba]

        # requete pour la modification
        query = "UPDATE poste SET nom =:nom, salaire =:salaire, descri =:descri WHERE rowid =:id"

        db.execute(query,{
            "nom" : Anarana,
            "salaire" : karama,
            "descri" : mombamomba,
            "id" : self.id
        })

        connection.commit()
        # connection.close()
        # self.buton_modifier.setVisible(False)
        # self.close()
        listes = ajout_poste()
        self.tableau.setRowCount(len(listes))
        for row,rowdata in enumerate(listes):
            for col,value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)


        self.titre_poste.setVisible(False)
        # self.buton_effacer.setVisible(False)
        self.nom_poste_input.setVisible(False)
        self.nom_poste.setVisible(False)
        self.salaire_poste.setVisible(False)
        self.salaire_poste_input.setVisible(False)
        self.descri_poste.setVisible(False)
        self.descri_poste_input.setVisible(False)


    def Effacer(self):
        
        ligne = self.tableau.selectedItems()
        conn = sqlite3.connect("gestion.db")
        cu = conn.cursor()
        cu.execute("DELETE FROM poste WHERE rowid =:id",{"id":self.id})


        conn.commit()
        conn.close()
        listes = ajout_poste()
        self.tableau.setRowCount(len(listes))
        for row,rowdata in enumerate(listes):
            for col,value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)


        msg_box = QMessageBox()
        msg_box.setWindowTitle('Succes')
        msg_box.setText('poste effacer !')
        msg_box.setIcon(QMessageBox.Information)

        # Stylisation du QMessageBox
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: green;
                color: white;
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

        self.titre_poste.setVisible(False)
        # self.buton_effacer.setVisible(False)
        self.nom_poste_input.setVisible(False)
        self.nom_poste.setVisible(False)
        self.salaire_poste.setVisible(False)
        self.salaire_poste_input.setVisible(False)
        self.descri_poste.setVisible(False)
        self.descri_poste_input.setVisible(False)
        



    def retour_fenetre1(self):
        self.deconnecter.show()    
        self.hide()


    def ajouter_poste(self):
        self.create_account_window = AjoutPoste()
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

class AjoutPoste(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter nouveau poste")
        self.resize(600,600)

        self.welcome_label = QLabel(self)
        self.welcome_label.setText("GESTION DE COMMANDE")
        self.welcome_label.setStyleSheet("font-size:16px;font-family:arial;font-weight: bolder;color:white")
        self.welcome_label.setGeometry(20, 30, 400, 60)
        
        self.image = QLabel(self)
        image = QPixmap("./images/sieze.jpg")
        size = image.scaled(600,600)
        self.image.setPixmap(size)

        self.ajout_post = QLabel(self, text="ajouter nouveau poste")
        self.ajout_post.setGeometry(20,100,500,30)
        self.ajout_post.setStyleSheet("font-size:30px;font-family:arial;color:#3c1101")

        self.nom_poste =QLabel(self, text="Titre :")
        self.nom_poste.setGeometry(20,150,120,30)
        self.nom_poste.setStyleSheet("font-size:20px;color:white")
        self.nom_poste_input = QLineEdit(self)
        self.nom_poste_input.setGeometry(130,150,250,30)
        self.nom_poste_input.setStyleSheet("border-radius:10px;padding:5px")


        self.salaire_poste =QLabel(self, text="Salaire :")
        self.salaire_poste.setGeometry(20,200,120,30)
        self.salaire_poste.setStyleSheet("font-size:20px;color:white")
        self.salaire_poste_input = QLineEdit(self)
        self.salaire_poste_input.setGeometry(130,200,250,30)
        self.salaire_poste_input.setStyleSheet("border-radius:10px;padding:5px")

        self.descri_poste =QLabel(self, text="descri :")
        self.descri_poste.setGeometry(20,250,120,30)
        self.descri_poste.setStyleSheet("font-size:20px;color:white")
        self.descri_poste_input = QLineEdit(self)
        self.descri_poste_input.setGeometry(130,250,250,200)
        self.descri_poste_input.setStyleSheet("border-radius:10px;padding:5px")



        self.enregistrer = QPushButton(self, text="Enregistrer")
        self.enregistrer.setGeometry(130,500,100,40)
        self.enregistrer.setStyleSheet("color:white;font-size:20px;border-radius:10px;background-color:green")
        self.enregistrer.setCursor(Qt.PointingHandCursor)
        self.enregistrer.clicked.connect(self.Enregistrer)

    def Enregistrer(self):
        if not self.nom_poste_input.text() or not self.salaire_poste_input.text() or not self.descri_poste_input.text() :
            # QMessageBox.warning(self, 'Champs vides', 'Veuillez remplir tous les champs.')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Erreur')
            msg_box.setText('Champs vides ! Veuillez remplir tous les champs.')
            msg_box.setIcon(QMessageBox.Warning)

            # Stylisation du QMessageBox
            msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: yellow;
                    color: white;
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

            return
            
        nom = self.nom_poste_input.text()
        salaire = self.salaire_poste_input.text()
        descri = self.descri_poste_input.text()
        listes = insertion_poste(nom,salaire,descri)

        self.nom_poste_input.clear()
        self.salaire_poste_input.clear()
        self.descri_poste_input.clear()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableau_poste = QDialog()
    ui = Tableau_poste_ui()
    tableau_poste.show()
    sys.exit(app.exec_()) 