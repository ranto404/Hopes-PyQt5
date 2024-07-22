import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QPushButton, QSpinBox, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QFontDatabase

import sys

class login_ui(QWidget):
    def __init__(self):
        super().__init__()

        login.setWindowTitle("Se connecter dans la gestion")
        login.resize(600,600)

        self.imageFont =QLabel(self)
        self.setGeometry(0,0,600,600)
        imageFont = QPixmap("./images/image2.jpg")
        size = imageFont.scaled(600,600)
        self.imageFont.setPixmap(size)


        self.image =QLabel(self)
        self.image.setGeometry(10,10,30,30)
        self.image.setStyleSheet("border:2px solid white;border-radius:10px")
        image = QPixmap("./images/logo.png")
        size = image.scaled(30,30)
        self.image.setPixmap(size)
        # QFontDatabase.addApplicationFont("chemin de votre font")
        # font = QFont()
        # font.setFamily("nom de font")
        # self.Titre.setFont(font)


        self.titre = QLabel(login, text="GESTION MEUBLEsPLUS-MADA")
        self.titre.setGeometry(0,50,500,30)
        self.titre.setStyleSheet("font-size:20px;color:black;font-weight:bold")
        self.titre.setAlignment(Qt.AlignCenter)

        self.email = QLabel(login, text="Adresse éléctronique :")
        self.email.setGeometry(100,150,300,20)
        self.email.setStyleSheet("font-size:16px")
        self.email_input = QLineEdit(login)
        self.email_input.setGeometry(100,185,300,30)
        self.email_input.setPlaceholderText("Votre adresse éléctronique")
        self.email_input.setStyleSheet("font-size:16px;border-radius:10px;border:1px solid black;padding:5px")

        self.mdp = QLabel(login, text="Mot de passe :")
        self.mdp.setGeometry(100,230,300,20)
        self.mdp.setStyleSheet("font-size:16px")
        self.password_input = QLineEdit(login)
        self.password_input.setGeometry(100,265,300,30)
        self.password_input.setPlaceholderText("Votre mot de passe")
        self.password_input.setStyleSheet("font-size:16px;border-radius:10px;border:1px solid black;padding:5px")
        self.password_input.setEchoMode(QLineEdit.Password)


        self.bouton_connecter = QPushButton(login, text="connexion")
        self.bouton_connecter.setGeometry(150,330,200,30)
        self.bouton_connecter.setStyleSheet("font-size:20px;background-color:green;border-radius:10px;color:white")
        self.bouton_connecter.setCursor(Qt.PointingHandCursor)
        self.bouton_connecter.clicked.connect(self.login)


        self.bouton_creer = QPushButton(login, text="créer un compte")
        self.bouton_creer.setGeometry(150,375,200,30)
        self.bouton_creer.setStyleSheet("font-size:20px;background-color:blue;border-radius:10px;color:white")
        self.bouton_creer.setCursor(Qt.PointingHandCursor)
        self.bouton_creer.clicked.connect(self.create_account)


    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
    
        if email != "" and password != "":
            if self.check_credentials(email, password):
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Succes')
                msg_box.setText('Connexion réussite !')
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

                # Changement de la police du texte du QMessageBox
                font = QFont()
                font.setPointSize(16)
                msg_box.setFont(font)

                msg_box.exec_()
                
                self.open_main_window()
                self.hide()  # Fermez la fenêtre de connexion
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Erreur')
                msg_box.setText('Erreur de la connexion, Identifiant incorrecte !')
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

                # Changement de la police du texte du QMessageBox
                font = QFont()
                font.setPointSize(16)
                msg_box.setFont(font)

                msg_box.exec_()
                
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Succes')
            msg_box.setText('Erreur de connexion veuillez saisir votre email et mot de passe !')
            msg_box.setIcon(QMessageBox.Warning)

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

            font = QFont()
            font.setPointSize(16)
            msg_box.setFont(font)

            msg_box.exec_()

        self.email_input.clear()
        self.password_input.clear()
        self.close()
        
            
    
    def open_main_window(self):
        from main_app_window import MainApplication_ui
        self.main_app_window = MainApplication_ui(self)
        self.main_app_window.show() 
        self.close()

        
    def check_credentials(self, email, password):
        conn = sqlite3.connect('gestion.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM comptes WHERE email = ? AND password = ?", (email, password))
        result = cursor.fetchone()

        conn.close()

        # identifiants corrects
        if result:
            return True
        else:
            return False

    def create_account(self):
        self.create_account_window = CreateAccountWindow()
        self.create_account_window.show()
        self.close()


class CreateAccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Créer un compte")
        self.resize(400,400)

        self.email = QLabel(self, text="Email :")
        self.email.setGeometry(20,60,50,20)
        self.email.setStyleSheet("font-size:16px")
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(20,85,300,30)
        self.email_input.setStyleSheet("font-size:16px;border-radius:10px")

        self.mdp = QLabel(self, text="Mot de passe :")
        self.mdp.setGeometry(20,140,300,20)
        self.mdp.setStyleSheet("font-size:16px")
        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(20,165,300,30)
        self.password_input.setStyleSheet("font-size:16px;border-radius:10px")

        self.mdp = QLabel(self, text="Confirmer :")
        self.mdp.setGeometry(20,220,300,20)
        self.mdp.setStyleSheet("font-size:16px")
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setGeometry(20,245,300,30)
        self.confirm_password_input.setStyleSheet("font-size:16px;border-radius:10px")

        self.bouton_connecter = QPushButton(self, text="créer")
        self.bouton_connecter.setGeometry(80,300,200,30)
        self.bouton_connecter.setStyleSheet("font-size:20px;background-color:green;border-radius:10px;color:white")
        self.bouton_connecter.setCursor(Qt.PointingHandCursor)
        self.bouton_connecter.clicked.connect(self.create_account)
        

      

    def create_account(self):
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password == confirm_password:
            conn = sqlite3.connect('gestion.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO comptes(email, password) VALUES (?, ?)", (email, password))

            conn.commit()
            conn.close()

            QMessageBox.information(self, "Compte créé", "Votre compte a été créé avec succès!")
        else:
            QMessageBox.warning(self, "Erreur", "Les mots de passe ne correspondent pas.")

        self.hide()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = QDialog()
    ui = login_ui()
    login.show()
    sys.exit(app.exec_())
