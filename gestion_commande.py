from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel,QPushButton, QLineEdit, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from fonction import insertion, ajout, insertion_client
import sys


class Commande_ui(QWidget):
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

        
        self.titre = QLabel(self, text=" Gestion de Commande MeublePlus-MADA")
        self.titre.setStyleSheet("font-family:arial;font-size:35px;font-family:Arial;font-weight: bold;color:#3c1101")
        self.titre.setGeometry(100, 50, 1000, 60)
        self.titre.setAlignment(Qt.AlignCenter)


        self.bouton_ajout_produit = QPushButton(self, text="liste des produits")
        self.bouton_ajout_produit.setGeometry(400,200,400,50)
        self.bouton_ajout_produit.setStyleSheet("QPushButton{font-size: 20px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_produit.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_produit.clicked.connect(self.ajouter_tableau_produit)


        self.bouton_ajout_client = QPushButton(self, text="liste des clients")
        self.bouton_ajout_client.setGeometry(400,300,400,50)       
        self.bouton_ajout_client.setStyleSheet("QPushButton{font-size: 20px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_client.clicked.connect(self.ajouter_tableau_client)

        self.bouton_ajout_commande = QPushButton(self, text="commande")
        self.bouton_ajout_commande.setGeometry(400,400,400,50)        
        self.bouton_ajout_commande.setStyleSheet("QPushButton{font-size: 20px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold;font-family:arial}QPushButton:hover{font-size:26px;background-color:cyan;color:orange})")
        self.bouton_ajout_commande.setCursor(Qt.PointingHandCursor)
        self.bouton_ajout_commande.clicked.connect(self.ajouter_commande)

        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1150, 20, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)

    def ajouter_tableau_produit(self):
        from tableau_produit import Tableau_produit_ui
        self.tableau_produit = Tableau_produit_ui(self)
        self.tableau_produit.show() 
        self.close()

    def ajouter_tableau_client(self):
        from tableau_client import Tableau_client_ui
        self.tableau_client = Tableau_client_ui(self)
        self.tableau_client.show() 
        self.close()

    def ajouter_commande(self):
        from gestion_contenir import Contenir_ui
        self.gestion_contenir = Contenir_ui(self)
        self.gestion_contenir.show() 
        self.close()


    def retour_fenetre1(self):
        self.retour.show()    
        self.hide()



    





if __name__ == "__main":
    app = QApplication(sys.argv)
    commande = Commande_ui()
    # ui = Commande_ui()
    commande.show()
    sys.exit(app.exec_())