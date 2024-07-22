import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QLineEdit, QDateTimeEdit, QComboBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QFont

from fonction import insertion_contenir

import sqlite3
from base import *


class EnterLineEdit(QLineEdit):
    enterPressed = pyqtSignal()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit()


class Contenir_ui(QWidget):

    last_row_used = 0
    def __init__(self, gestion_commande):
        super().__init__()
        self.setWindowTitle("Gestion de Commande d'immeuble")
        self.resize(1500,1500)
        # self.setStyleSheet("background-color:#012b3c")
        self.deconnecter = gestion_commande


        self.imageFont =QLabel(self)
        self.setGeometry(0,0,1500,1500)
        imageFont = QPixmap("./images/image2.jpg")
        size = imageFont.scaled(1500,1500)
        self.imageFont.setPixmap(size)

        self.image =QLabel(self)
        self.image.setGeometry(20,20,70,70)
        self.image.setStyleSheet("border:2px solid white;border-radius:10px")
        image = QPixmap("./images/logo.png")
        size = image.scaled(70,70)
        self.image.setPixmap(size)



        self.Titre = QLabel(self, text="Commande d'Immeuble")
        self.Titre.setGeometry(500,30,310,40)
        self.Titre.setStyleSheet("font-size:25px;color:#3c1101;font-weight:bold")

        
        
        self.nom_client =QLabel(self, text="Nom")
        self.nom_client.setGeometry(20,100,120,20)
        self.nom_client.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.nom_client_combo = QComboBox(self)
        self.nom_client_combo.setGeometry(140,100,250,25)
        self.nom_client_combo.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")
        self.nom_client_combo.currentIndexChanged.connect(self.display_client_details)


        self.prenom_client =QLabel(self, text="Prénom")
        self.prenom_client.setGeometry(20,140,120,20)
        self.prenom_client.setStyleSheet("font-size:16px;color:;color:#3c1101;font-weight:bold")
        self.prenom_client_input = QLineEdit(self)
        self.prenom_client_input.setGeometry(140,140,250,25)
        self.prenom_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:;color:#3c1101;padding:5px")

        self.adresse_client =QLabel(self, text="Adresse")
        self.adresse_client.setGeometry(20,180,120,20)
        self.adresse_client.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.adresse_client_input = QLineEdit(self)
        self.adresse_client_input.setGeometry(140,180,250,25)
        self.adresse_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")

        self.num_client =QLabel(self, text="Téléphone")
        self.num_client.setGeometry(20,220,120,20)
        self.num_client.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.num_client_input = QLineEdit(self)
        self.num_client_input.setGeometry(140,220,250,25)
        self.num_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")

        self.code_client =QLabel(self, text="CIN/Passport :")
        self.code_client.setGeometry(20,260,120,20)
        self.code_client.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.code_client_input = QLineEdit(self)
        self.code_client_input.setGeometry(140,260,250,25)
        self.code_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")
        
        self.num_commd =QLabel(self, text="Numero")
        self.num_commd.setGeometry(850,100,120,20)
        self.num_commd.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.num_commd_input = QLineEdit(self)
        self.num_commd_input.setGeometry(970,100,250,25)
        self.num_commd_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")

        self.date_commd =QLabel(self, text="Date :")
        self.date_commd.setGeometry(850,140,120,20)
        self.date_commd.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.date_commd_input = QDateTimeEdit(self)
        self.date_commd_input.setGeometry(970,140,250,25)
        self.date_commd_input.setStyleSheet("border-radius:10px;font-size:16px;color:#3c1101;padding:5px")

        self.paie =QLabel(self, text="Paie :")
        self.paie.setGeometry(850,180,120,20)
        self.paie.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.paie_combo =QComboBox(self)
        self.paie_combo.setStyleSheet("border-radius:10px;color:#3c1101;font-size:16px;padding:5px")
        self.paie_combo.addItem("Virement_banquaire")
        self.paie_combo.addItem("Espece")
        self.paie_combo.setGeometry(970,180,250,25)

        self.produit =QLabel(self, text="Selectionner Produits :")
        self.produit.setGeometry(850,220,200,20)
        self.produit.setStyleSheet("font-size:16px;color:#3c1101;font-weight:bold")
        self.product_combo =QComboBox(self) 
        self.product_combo.setStyleSheet("border-radius:10px;color:#3c1101;font-size:16px")   
        self.product_combo.setGeometry(850,250,250,25)

        self.product_table = QTableWidget(self)
        self.product_table.setGeometry(200,300,900,300)
        self.product_table.verticalHeader().setVisible(False)

        self.product_table.setStyleSheet("""
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
        self.product_table.setColumnCount(9)
        self.product_table.setHorizontalHeaderLabels(["Nom", "Désignation", "Quantité", "Unité", "Prix Unitaire", "MontantP", "MontantC", "Reste", "Quantité"])
        self.product_table.setColumnWidth(0,100)
        self.product_table.setColumnWidth(1,100)
        self.product_table.setColumnWidth(2,100)
        self.product_table.setColumnWidth(3,100)
        self.product_table.setColumnWidth(4,100)
        self.product_table.setColumnWidth(5,100)
        self.product_table.setColumnWidth(6,100)
        self.product_table.setColumnWidth(7,100)
        self.product_table.setColumnWidth(8,100)
        
        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1150, 30, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)

        self.commander_button = QPushButton(self, text="Net à payer :")
        self.commander_button.setGeometry(750, 610, 100, 30)
        self.commander_button.setStyleSheet("QPushButton{font-size: 16px;padding:5px;font-weight:bold;background-color:orange;color:white;border-radius:10px}QPushButton:hover{font-size:16px;color:blue}")
        self.commander_button.setCursor(Qt.PointingHandCursor)
        self.commander_button.clicked.connect(self.calculate_total_amount_and_display)

        self.total_amount_input = QLineEdit(self)
        self.total_amount_input.setGeometry(900, 610, 200, 30)
        self.total_amount_input.setStyleSheet("font-size: 12px; background-color:white;color:#3c1101;border-radius:10px;padding:5px")
        self.total_amount_input.setReadOnly(True)
        self.total_amount_input.setPlaceholderText("Ar/HT")

        self.creer_button = QPushButton(self, text="Enregistrer")
        self.creer_button.setGeometry(750, 650, 100, 30)
        self.creer_button.setStyleSheet("font-size: 12px; background-color:green;color:white;font-weight:bold;border-radius:10px")
        self.creer_button.setCursor(Qt.PointingHandCursor)
        self.creer_button.clicked.connect(self.Enregistrer)

        self.cont_button = QPushButton(self, text="Details")
        self.cont_button.setGeometry(900, 650, 100, 30)
        self.cont_button.setStyleSheet("font-size: 12px; background-color:blue;color:white;border-radius:10px")
        self.cont_button.setCursor(Qt.PointingHandCursor)
        self.cont_button.clicked.connect(self.ajouter_tableau_contenir)

        self.product_combo.currentIndexChanged.connect(self.display_product_details)
        self.load_products()
        self.load_clients()


    def ajouter_tableau_contenir(self):
        from contenir import Tableau_contenir_ui
        self.contenir = Tableau_contenir_ui(self)
        self.contenir.show() 
        self.close()

    
    def Enregistrer(self):
        self.product_table.setRowCount(0)

        if not self.num_client_input.text() or not self.date_commd_input.text() or not self.nom_client_combo.currentText() or not self.paie_combo.currentText() or not self.total_amount_input.text() :
            # QMessageBox.warning(self, 'Champs vides', 'Veuillez remplir tous les champs.')
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Erreur')
            msg_box.setText('Erreur ! Veuillez remplir les champs vides !')
            msg_box.setIcon(QMessageBox.Warning)

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
            
            return
        
        for row in range(self.product_table.rowCount()):
            for col in range(self.product_table.columnCount()):
                item = self.product_table.item(row, col)
            if item:
                self.product_table.takeItem(row, col)

        num = self.num_commd_input.text()
        date = self.date_commd_input.text()
        nom = self.nom_client_combo.currentText()
        paie = self.paie_combo.currentText()
        montant = self.total_amount_input.text()
        listes = insertion_contenir(num,date,nom,paie,montant)

        self.date_commd_input.clear()
        self.num_client_input.clear()
        self.prenom_client_input.clear()
        self.adresse_client_input.clear()
        self.num_client_input.clear()
        self.code_client_input.clear()
        # self.product_table.clear()
        self.total_amount_input.clear()
        

        


        msg_box = QMessageBox()
        msg_box.setWindowTitle('Succes')
        msg_box.setText('Excel générer avec succès !')
        msg_box.setIcon(QMessageBox.Information)

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
        
    

    def load_clients(self):
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()
        cursor.execute("SELECT nom FROM clients")
        clients = cursor.fetchall()
        for client in clients:
            self.nom_client_combo.addItem(client[0])
        connection.close()

    def display_client_details(self):
        selected_name = self.nom_client_combo.currentText()
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()
        cursor.execute("SELECT prenom, adresse, phone, cin FROM clients WHERE nom = ?", (selected_name,))
        client_details = cursor.fetchone()
        if client_details:
            self.prenom_client_input.setText(client_details[0])
            self.adresse_client_input.setText(client_details[1])
            self.num_client_input.setText(client_details[2])
            self.code_client_input.setText(client_details[3])
        connection.close()




    def load_products(self):
        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()

        cursor.execute("SELECT nom, designation, quantite, unite, prix_unitaire, montant_total FROM products")
        products = cursor.fetchall()

        for product in products:
            self.product_combo.addItem(product[0])

        connection.close()

    def display_product_details(self, index):
        product_name = self.product_combo.itemText(index)

        connection = sqlite3.connect('gestion.db')
        cursor = connection.cursor()

        cursor.execute("SELECT nom, designation, quantite, unite, prix_unitaire, montant_total FROM products WHERE nom = ?", (product_name,))
        product_details = cursor.fetchone()

        if product_details:
            row_position = self.product_table.rowCount()
            self.product_table.insertRow(row_position)
            for col, detail in enumerate(product_details):
                self.product_table.setItem(row_position, col, QTableWidgetItem(str(detail)))


            self.quantity_input = EnterLineEdit()
            self.product_table.setCellWidget(row_position, 8, self.quantity_input)
        
            self.quantity_input.enterPressed.connect(lambda: self.calculate_total_amount(row_position))

            Contenir_ui.last_row_used = row_position

        else:
            print("Aucun détail de produit trouvé pour", product_name)

        connection.close()

    def calculate_total_amount(self,row):
        quantity_input = self.product_table.cellWidget(row, 8)
        quantity_ordered = int(quantity_input.text())

        price_item = self.product_table.item(row, 4)
        if price_item is not None:
            price_per_unit = float(price_item.text())
            total_amount = quantity_ordered * price_per_unit
            self.product_table.setItem(row, 6, QTableWidgetItem(str(total_amount)))

            montant_item = self.product_table.item(row, 5)
            if montant_item is not None:
                montant_total = float(montant_item.text())
                reste = montant_total - total_amount
                self.product_table.setItem(row, 7, QTableWidgetItem(str(reste)))

    
    def calculate_total_amount_and_display(self):
        total = 0
        for row in range(self.product_table.rowCount()):
            montant_item = self.product_table.item(row, 6)
            if montant_item is not None:
                total += float(montant_item.text())
        self.total_amount_input.setText(str(total))




        
    def retour_fenetre1(self):
        self.deconnecter.show()    
        self.hide()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    contenir_window = QDialog()
    ui = Contenir_ui()
    contenir_window.show()
    sys.exit(app.exec_()) 