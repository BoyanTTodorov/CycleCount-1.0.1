from fileinput import filename
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
import sys
from os import path
from PyQt6.uic import loadUiType
FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), 'main.ui'))
import pandas as pd
import func

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Browse_Files()     
        self.setFixedSize(self.size())

    def getfiles(self):
        filename = QFileDialog.getOpenFileName(self,'Single File','C:\'','*.xlsx')
        df = pd.read_excel(filename[0])
        df = df['Storage Bin']
        func.update_cycle_counting(df)

        QMessageBox.about(self, "Database", " UPDATED ")
        
        print('#########################################')
        print(f'All Databases successfully updated')
        print('#########################################')
        
    def Browse_Files(self):
        print('####################')
        print('Please select file')
        print('####################')
        self.btn_post.clicked.connect(self.getfiles)

def main():
    app = QApplication(sys.argv)
    window = Main()
    func.db_connect(func.path)
    window.show()
    app.exec()

if __name__ == '__main__':
    main()