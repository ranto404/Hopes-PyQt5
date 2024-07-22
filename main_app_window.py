import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap



class MainApplication_ui(QWidget):
    def __init__(self, login):
        super().__init__()
        self.setWindowTitle("Main Application")
        self.resize(1500, 1500)
        self.deconnecter = login
        
          

        self.image =QLabel(self)
        self.setGeometry(0,0,1500,1500)
        image = QPixmap("./images/image2.jpg")
        size = image.scaled(1500,1500)
        self.image.setPixmap(size)  

        self.welcome_label = QLabel(self)
        self.welcome_label.setText("BIENVENUE DANS NOTRE SOCIETE MeublePlus-MADA")
        self.welcome_label.setStyleSheet("font-family:arial;font-size:30px;font-family:Arial;font-weight: bold;color:#3c1101")
        self.welcome_label.setGeometry(100, 100, 1000, 60)
        self.welcome_label.setAlignment(Qt.AlignCenter)


        self.bouton_personnel = QPushButton(self, text="Gestion de personnel")
        self.bouton_personnel.setGeometry(400,300,400,50)
        self.bouton_personnel.setStyleSheet("font-size: 16px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold")
        self.bouton_personnel.setCursor(Qt.PointingHandCursor)
        self.bouton_personnel.clicked.connect(self.gestion_personnel)


        self.bouton_commande = QPushButton(self, text="Gestion de commande")
        self.bouton_commande.setGeometry(400,400,400,50)
        self.bouton_commande.setStyleSheet("font-size:16px;background-color:#8f028f77;color:#3c1101;border-radius:20px;font-weight: bold")
        self.bouton_commande.setCursor(Qt.PointingHandCursor)
        self.bouton_commande.clicked.connect(self.gestion_commande)


        # self.bouton_deconn = QPushButton(self)
        # self.bouton_deconn.setGeometry(1150, 20, 50, 50)
        # self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        # self.bouton_deconn.setToolTip('Fermer l\'application')
        # self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        # self.bouton_deconn.clicked.connect(self.retour_fenetre1)


    # def retour_fenetre1(self):
    #     self.deconnecter.show()    
    #     self.hide()

    def gestion_personnel(self):
        from gestion_personnel import Personnel_ui
        self.pers = Personnel_ui(self)
        self.pers.show()
        self.close()

    def gestion_commande(self):
        from gestion_commande import Commande_ui
        self.comm = Commande_ui(self)
        self.comm.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app_window = QDialog()
    ui = MainApplication_ui()
    main_app_window.show()
    sys.exit(app.exec_()) 