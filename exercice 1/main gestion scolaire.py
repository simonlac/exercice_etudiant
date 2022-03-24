import sys
import gestion_de_scolarite as F
from élève import*
from PyQt5 import QtWidgets , QtCore
list_etudiant = []
class fngestion(QtWidgets.QMainWindow, F.Ui_MainWindow):



    def __init__(self, parent=None):

        super(fngestion, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion de scolarité")
    @QtCore.pyqtSlot()
    def on_btvalidation_clicked(self):
        nbetudiant = self.linenb.text()
        nometudiant = self.linenom.text()
        e = etudiant(nometudiant,nbetudiant)
        list_etudiant.append(e)
        self.afficheeleve.append(e.__str__())




def main():
    app = QtWidgets.QApplication(sys.argv)
    form = fngestion()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()