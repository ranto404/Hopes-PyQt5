import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QLineEdit, QDateTimeEdit, QComboBox, QTableWidget, QTableWidgetItem
import pandas as pd
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QFont, QIcon
from fonction import insertion, ajout_contenir
from fpdf import FPDF
from base import *
db, connection = base()


class Tableau_contenir_ui(QWidget):
    def __init__(self, gestion_contenir):
        super().__init__()
        self.setWindowTitle("Gestion de Commande d'immeuble")
        # self.setStyleSheet("background-color:#012b3c")
        self.resize(1500,1500)
        self.deconnecter = gestion_contenir

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

        self.titre_contenir = QLabel(self, text="DETAILS COMMANDES")
        self.titre_contenir.setGeometry(500,50,500,50)
        self.titre_contenir.setStyleSheet("font-size:40px;font-style:normal;font-weight:bold;color:#3c1101")


        self.titre_client = QLabel(self, text="facture commande")
        self.titre_client.setGeometry(20,150,500,30)
        self.titre_client.setStyleSheet("font-size:20px;font-style:normal;font-weight:bold;color:#3c1101")
        self.titre_client.setVisible(False)

        self.numero_client =QLabel(self, text="Numero :")
        self.numero_client.setGeometry(20,200,120,30)
        self.numero_client.setStyleSheet("font-size:20px;color:#3c1101;font-weight:bold")
        self.numero_client.setVisible(False)
        self.numero_client_input = QLineEdit(self)
        self.numero_client_input.setGeometry(130,200,250,30)
        self.numero_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding:5px")
        self.numero_client_input.setVisible(False)


        self.date_client =QLabel(self, text="Date :")
        self.date_client.setGeometry(20,250,120,30)
        self.date_client.setStyleSheet("font-size:20px;color:#3c1101;font-weight:bold")
        self.date_client.setVisible(False)
        self.date_client_input = QLineEdit(self)
        self.date_client_input.setGeometry(130,250,250,30)
        self.date_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding:5px")
        self.date_client_input.setVisible(False)


        self.nom_client =QLabel(self, text="Nom :")
        self.nom_client.setGeometry(20,300,120,30)
        self.nom_client.setStyleSheet("font-size:20px;color:#3c1101;font-weight:bold")
        self.nom_client.setVisible(False)
        self.nom_client_input = QLineEdit(self)
        self.nom_client_input.setGeometry(130,300,250,30)
        self.nom_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding:5px")
        self.nom_client_input.setVisible(False)

        self.paie_client =QLabel(self, text="Paiement :")
        self.paie_client.setGeometry(20,350,120,30)
        self.paie_client.setStyleSheet("font-size:20px;color:#3c1101;font-weight:bold")
        self.paie_client.setVisible(False)
        self.paie_client_input = QLineEdit(self)
        self.paie_client_input.setGeometry(130,350,250,30)
        self.paie_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding:5px")
        self.paie_client_input.setVisible(False)

        self.montant_client =QLabel(self, text="Montant :")
        self.montant_client.setGeometry(20,400,120,30)
        self.montant_client.setStyleSheet("font-size:20px;color:#3c1101;font-weight:bold")
        self.montant_client.setVisible(False)
        self.montant_client_input = QLineEdit(self)
        self.montant_client_input.setGeometry(130,400,250,30)
        self.montant_client_input.setStyleSheet("border-radius:10px;font-size:16px;color:black;padding:5px")
        self.montant_client_input.setVisible(False)


        self.annonce = QLabel(self)
        self.annonce.setGeometry(100,550,300,30)
        self.annonce.setText("Veuillez séléctionner une ligne pour faire l'action :")
        self.annonce.setStyleSheet("fonte-size:40px;color:#3c1101;font-weight:bold;text-decoration: underline")

        self.buton_imprimer = QPushButton(self)
        self.buton_imprimer.setGeometry(100,600,100,30)
        self.buton_imprimer.setText("IMPRIMER")
        self.buton_imprimer.setCursor(Qt.PointingHandCursor)
        self.buton_imprimer.setStyleSheet("background-color:blue;font-size:16px;color:white;border-radius:10px")
        self.buton_imprimer.enterEvent = self.ouvre
        self.buton_imprimer.leaveEvent = self.ferme
        self.buton_imprimer.setEnabled(False)
        # self.buton_imprimer.setVisible(False)
        
        self.recherche_input = QLineEdit(self)
        self.recherche_input.setGeometry(600,150,200,30)
        self.recherche_input.setStyleSheet("font-size:20px;border-radius:10px;color:black;background-color:white;border:1px solid #3c1101")
        self.btn_recherche = QPushButton(self, text="recherche")
        self.btn_recherche.setGeometry(830,150,100,30)
        self.btn_recherche.setStyleSheet("font-size:20px;border-radius:10px;color:white;background-color:orange")
        self.btn_recherche.clicked.connect(self.Rechercher)

        
        self.buton_effacer = QPushButton(self)
        self.buton_effacer.setGeometry(250,600,100,30)
        self.buton_effacer.setText("Effacer")
        self.buton_effacer.setCursor(Qt.PointingHandCursor)
        self.buton_effacer.setStyleSheet("background-color:red;color:white;border-radius:10px")
        self.buton_effacer.enterEvent = self.ouvrir
        self.buton_effacer.leaveEvent = self.fermer
        self.buton_effacer.setEnabled(False)
        self.buton_effacer.clicked.connect(self.Effacer)
        # self.buton_effacer.setVisible(False)

        self.buton_excel = QPushButton(self)
        self.buton_excel.setGeometry(400,600,100,30)
        self.buton_excel.setText("EXCEL")
        self.buton_excel.setCursor(Qt.PointingHandCursor)
        self.buton_excel.setStyleSheet("background-color:green;font-size:16px;color:white;border-radius:10px;font-weight:bold")
        self.buton_excel.enterEvent = self.ouvr
        self.buton_excel.leaveEvent = self.ferm
        self.buton_excel.setEnabled(False)
        self.buton_excel.clicked.connect(self.print)
        # self.buton_excel.setVisible(False)


        self.text = QLabel(self, text="selectionner dans le tableau pour effacer")
        self.text.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text.setVisible(False)
        
        self.text1 = QLabel(self, text="selectionner un ligne dans le tableau pour imprimer")
        self.text1.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text1.setVisible(False)

        self.text2 = QLabel(self, text="selectionner un ligne dans le tableau pour envoyer")
        self.text2.setStyleSheet("""QLabel{color:black;font-size:12px;background-color:orange;padding:5px}""")
        self.text2.setVisible(False)

        

        self.tableau = QTableWidget(self)
        self.tableau.setGeometry(600,200,600,400)
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

        self.tableau.setColumnCount(6)
        self.tableau.setRowCount(20)
        self.tableau.setHorizontalHeaderLabels([
           "id", "numero","date","nom", "paiement", "montant"
        ])
        self.tableau.setColumnWidth(0,50)
        self.tableau.setColumnWidth(1,100)
        self.tableau.setColumnWidth(2,100)
        self.tableau.setColumnWidth(3,100)
        self.tableau.setColumnWidth(4,100)
        self.tableau.setColumnWidth(5,150)
        self.tableau.itemClicked.connect(self.Selectionner)
        
        listes=ajout_contenir()
        self.tableau.setRowCount(len(listes))
        for row, rowData in enumerate(listes):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)










        self.bouton_deconn = QPushButton(self)
        self.bouton_deconn.setGeometry(1200, 20, 50, 50)
        self.bouton_deconn.setIcon(QIcon('./images/close_icon.png'))
        self.bouton_deconn.setToolTip('Fermer l\'application')
        self.bouton_deconn.setCursor(Qt.PointingHandCursor)
        self.bouton_deconn.clicked.connect(self.retour_fenetre1)


        self.buton_imprimer.clicked.connect(self.generer_pdf)

    def Rechercher(self):
        mot= self.recherche_input.text()
        listes=ajout_contenir()
        self.tableau.setRowCount(len(listes))
        j=1
        for i in range(len(listes)):
            if mot in listes[i]:
                self.tableau.setRowCount(j)
                for col, value in enumerate(listes[i]):
                    item = QTableWidgetItem(str(value))
                    self.tableau.setItem(j-1,col,item)
                j += 1


    def ouvrir(self, event):
        self.text.setVisible(True)
        self.text.move(self.buton_effacer.pos() + QPoint(10, -20))
    def fermer(self, event):
        self.text.setVisible(False)

    def ouvre(self, event):
        self.text1.setVisible(True)
        self.text1.move(self.buton_imprimer.pos() + QPoint(10, -20))
    def ferme(self, event):
        self.text1.setVisible(False)
        
    def ouvr(self, event):
        self.text2.setVisible(True)
        self.text2.move(self.buton_excel.pos() + QPoint(10, 20))
    def ferm(self, event):
        self.text2.setVisible(False)

    def print(self):
        donnees_tableau = []
        for row in range(self.tableau.rowCount()):
            ligne = []
            for col in range(self.tableau.columnCount()):
                item = self.tableau.item(row, col)
                if item is not None:
                    ligne.append(item.text())
                else:
                    ligne.append("")
            donnees_tableau.append(ligne)

        # Convertir les données en DataFrame pandas
        df = pd.DataFrame(donnees_tableau, columns=["id", "numero","date","nom", "paiement", "montant"])

    # Sauvegarder le DataFrame dans un fichier Excel
        excel_output = "Fenetres_cont.xlsx"
        df.to_excel(excel_output, index=False)

        print("Fichier Excel généré avec succès :", excel_output)
        Excel = "C:\Program Files\Microsoft Office\Office16\excel.exe"
        subprocess.Popen([Excel, "Fenetres_cont.xlsx"])

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Succes')
        msg_box.setText('Excel générer avec succès !')
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
        



    def generer_pdf(self):
        pdf = FPDF()

        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Facture Commande MeublePlus', 0, 1, 'C')
                self.ln(10)  # Saut de ligne

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        

        # Récupérer les données des champs d'entrée
        numero = self.numero_client_input.text()
        date = self.date_client_input.text()
        nom = self.nom_client_input.text()
        paiement = self.paie_client_input.text()
        montant = self.montant_client_input.text()

        position_y = 40

        data_x = 10 

        pdf.set_xy(data_x, position_y)
        pdf.cell(200, 10, txt=f"Numéro: {numero}", ln=True, align='L')
        pdf.set_xy(data_x, pdf.get_y())
        pdf.cell(200, 10, txt=f"Date CO: {date}", ln=True, align='L')
        pdf.set_xy(data_x, pdf.get_y())
        pdf.cell(200, 10, txt=f"Nom: {nom}", ln=True, align='L')
        pdf.set_xy(data_x, pdf.get_y())
        pdf.cell(200, 10, txt=f"Paiement: {paiement}", ln=True, align='L')
        pdf.set_xy(data_x, pdf.get_y())
        pdf.cell(200, 10, txt=f"Montant: {montant}", ln=True, align='L')

        contact_x = 130 

        pdf.set_xy(contact_x, position_y)

        contact_info = """
        Contact :
        Adresse : [ByPass]
        Téléphone : [+23 23 000 32]
        E-mail : info@meublesplus.com
        Site web : www.meublesplus.com
        """

        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, contact_info, align="R")

        pdf.cell(200, 10, ln=True)
        pdf.cell(200, 10, ln=True)
        pdf.cell(200, 10, ln=True)

        pdf.set_font("Arial", size=12)
        mission_text = """
        Mission :
        Créations MeublesPlus s'engage à offrir des meubles de qualité exceptionnelle, conçus avec passion et artisanat, 
        pour créer des espaces de vie inspirants et fonctionnels pour nos clients.
        """
        pdf.multi_cell(0, 10, mission_text)



        pdf_output = "commande_immeuble.pdf"
        pdf.output(pdf_output)

        print("PDF généré avec succès.")

        import os
        os.startfile(pdf_output)

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Succes')
        msg_box.setText('Pdf générer avec succès !')
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
        



    def Selectionner(self,item):
        self.buton_excel.setVisible(True)
        self.buton_imprimer.setVisible(True)
        self.buton_effacer.setVisible(True)
        self.numero_client_input.setVisible(True)
        self.nom_client_input.setVisible(True)
        self.date_client_input.setVisible(True)
        self.montant_client_input.setVisible(True)
        self.paie_client_input.setVisible(True)
        self.titre_client.setVisible(True)
        self.nom_client.setVisible(True)
        self.date_client.setVisible(True)
        self.numero_client.setVisible(True)
        self.paie_client.setVisible(True)
        self.montant_client.setVisible(True)

        self.buton_effacer.setEnabled(True)
        self.buton_imprimer.setEnabled(True)
        self.buton_excel.setEnabled(True)


    
        row = item.row()
        col = item.column()
        valeur = item.text()
        self.id = self.tableau.item(row,0).text() 

        print(f"{row,col,valeur,id}")        
        modif = "SELECT * FROM contenir WHERE rowid = ?"
        # data = db.execute(modif, self.id)
        data = db.execute(modif, (self.id,))
        resultats = data.fetchall()
        print(resultats)


        self.numero_client_input.setText(str(resultats[0][0]))
        self.date_client_input.setText(str(resultats[0][1]))
        self.nom_client_input.setText(str(resultats[0][2]))
        self.paie_client_input.setText(str(resultats[0][3]))
        self.montant_client_input.setText(str(resultats[0][4]))
    
        
    def Effacer(self):
        instance_tableau_contenir_ui = Tableau_contenir_ui(gestion_contenir=None)
        ligne = self.tableau.selectedItems()
        conn = sqlite3.connect("gestion.db")
        cu = conn.cursor()
        cu.execute("DELETE FROM contenir WHERE rowid =:id",{"id":self.id})


        conn.commit()
        conn.close()
        listes = ajout_contenir()
        self.tableau.setRowCount(len(listes))
        for row,rowdata in enumerate(listes):
            for col,value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                self.tableau.setItem(row,col,item)


    def retour_fenetre1(self):
        self.deconnecter.show()    
        self.hide()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    Tableau_cont = QDialog()
    ui = Tableau_contenir_ui()
    Tableau_cont.show()
    sys.exit(app.exec_()) 