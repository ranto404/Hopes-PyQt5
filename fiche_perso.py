import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QLineEdit, QDateTimeEdit, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QFont

from fonction import insertion_fiche

import sqlite3
from base import *


class EnterLineEdit(QLineEdit):
    enterPressed = pyqtSignal()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit()


class Fiche_ui(QWidget):

    last_row_used = 0
    def __init__(self, gestion_personnel):
        super().__init__()
        self.setWindowTitle("Gestion de Commande d'immeuble")
        self.resize(1500,1500)
        # self.setStyleSheet("background-color:#012b3c")
        self.deconnecter = gestion_personnel

        self.imageFont =QLabel(self)
        self.setGeometry(0,0,1500,1500)
        imageFont = QPixmap("./images/image2.jpg")
        size = imageFont.scaled(1500,1500)
        self.imageFont.setPixmap(size)




        self.Titre = QLabel(self, text="Renseignement Personnels")
        self.Titre.setGeometry(450,30,500,40)
        self.Titre.setStyleSheet("font-size:30px;color:#3c1101;font-weight:bold")

        self.image =QLabel(self)
        self.image.setGeometry(30,30,70,70)
        self.image.setStyleSheet("border:2px solid white;border-radius:10px")
        image = QPixmap("./images/logo.png")
        size = image.scaled(70,70)
        self.image.setPixmap(size)

        
        # self.image2 =QLabel(self)
        # self.image2.setGeometry(350,300,600,300)
        # self.image2.setStyleSheet("border:2px solid white;border-radius:10px")
        # image2 = QPixmap("./images/imagePerso.jpg")
        # size = image2.scaled(600,300)
        # self.image2.setPixmap(size)


        # self.sous_titre = QLabel(self, text="personnel :")

        
        self.nom_perso =QLabel(self, text="Nom")
        self.nom_perso.setGeometry(200, 150,120,30)
        self.nom_perso.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.nom_perso_combo = QComboBox(self)
        self.nom_perso_combo.setGeometry(340,150,250,30)
        self.nom_perso_combo.setStyleSheet("border-radius:10px;color:black;font-size:16px;padding-left:5px")
        self.nom_perso_combo.currentIndexChanged.connect(self.display_perso_details)


        self.poste_perso =QLabel(self, text="Poste :")
        self.poste_perso.setGeometry(200,190,120,30)
        self.poste_perso.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.poste_perso_input = QLineEdit(self)
        self.poste_perso_input.setGeometry(340,190,250,30)
        self.poste_perso_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")

        self.num_fiche =QLabel(self, text="Numero :")
        self.num_fiche.setGeometry(200,230,120,30)
        self.num_fiche.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.num_fiche_input = QLineEdit(self)
        self.num_fiche_input.setGeometry(340,230,250,30)
        self.num_fiche_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")

        self.date_fiche =QLabel(self, text="Date :")
        self.date_fiche.setGeometry(200,270,120,30)
        self.date_fiche.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.date_fiche_input = QDateTimeEdit(self)
        self.date_fiche_input.setGeometry(340,270,250,30)
        self.date_fiche_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding-left:5px")

        self.conge =QLabel(self, text="Congé")
        self.conge.setGeometry(200,310,120,30)
        self.conge.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.conge_input =QLineEdit(self)
        self.conge_input.setStyleSheet("border-radius:10px;color:black;font-size:16px;font-size:16px;padding:5px")
        self.conge_input.setGeometry(340,310,250,30)

        self.evaluation =QLabel(self, text="Ajouter évaluation :")
        self.evaluation.setGeometry(200,370,250,30)
        self.evaluation.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.evaluation_input =QLineEdit(self) 
        self.evaluation_input.setStyleSheet("border-radius:10px;color:black;font-size:16px;background-color:white;padding-left:5px")   
        self.evaluation_input.setGeometry(200,410,380,70)

        
        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1200, 20, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)

        
        self.creer_button = QPushButton(self, text="Enregistrer")
        self.creer_button.setGeometry(750, 410, 100, 30)
        self.creer_button.setStyleSheet("font-size: 12px; background-color:green;color:white;border-radius:10px;font-weight:bold")
        self.creer_button.setCursor(Qt.PointingHandCursor)
        self.creer_button.clicked.connect(self.Enregistrer)

        self.cont_button = QPushButton(self, text="Details")
        self.cont_button.setGeometry(750, 450, 100, 30)
        self.cont_button.setStyleSheet("font-size: 12px; background-color:blue;color:white;border-radius:10px;font-weight:bold")
        self.cont_button.setCursor(Qt.PointingHandCursor)
        self.cont_button.clicked.connect(self.ajouter_tableau_fiche)

        self.load_perso()


    def ajouter_tableau_fiche(self):
        from details_perso import Tableau_fiche_ui
        self.details_perso = Tableau_fiche_ui(self)
        self.details_perso.show() 
        self.close()

    
    def Enregistrer(self):
        if not self.num_fiche_input.text() or not self.poste_perso_input.text() or not self.date_fiche_input.text() or not self.conge_input.text() or not self.evaluation_input.text() :
            # QMessageBox.warning(self, 'Champs vides', 'Veuillez remplir tous les champs.')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Erreur')
            msg_box.setText('Erreur ! veuillez remplir les champs vides !')
            msg_box.setIcon(QMessageBox.Warning)

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
        
        
        num = self.num_fiche_input.text()
        poste = self.poste_perso_input.text()
        date = self.date_fiche_input.text()
        nom = self.nom_perso_combo.currentText()
        conge = self.conge_input.text()
        evaluation = self.evaluation_input.text()
        listes = insertion_fiche(num,date,nom,poste,conge,evaluation)

        self.date_fiche_input.clear()
        self.num_fiche_input.clear()
        self.nom_perso_combo.clear()
        self.date_fiche_input.clear()
        self.conge_input.clear()
        self.evaluation_input.clear()
        self.poste_perso_input.clear()

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Succes')
        msg_box.setText('Excel générer avec succès !')
        msg_box.setIcon(QMessageBox.Information)

        # Stylisation du QMessageBox
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

        # Changement de la police du texte du QMessageBox
        font = QFont()
        font.setPointSize(16)
        msg_box.setFont(font)

        msg_box.exec_()
        

    def load_perso(self):
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()
        cursor.execute("SELECT nom FROM perso")
        postes = cursor.fetchall()
        for poste in postes:
            self.nom_perso_combo.addItem(poste[0])
        connection.close()

    def display_perso_details(self):
        selected_name = self.nom_perso_combo.currentText()
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()
        cursor.execute("SELECT date_embauche FROM perso WHERE nom = ?", (selected_name,))
        poste_details = cursor.fetchone()
        if poste_details:
            self.poste_perso_input.setText(poste_details[0])
        connection.close()


        
    def retour_fenetre1(self):
        self.deconnecter.show()    
        self.hide()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiche_window = QDialog()
    ui = Fiche_ui()
    fiche_window.show()
    sys.exit(app.exec_()) 