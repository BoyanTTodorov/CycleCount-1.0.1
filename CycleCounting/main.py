import sys
# import pandas as pd
# from datetime import datetime
from PyQt6 import QtWidgets
from myui import Ui_Form
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from queries import GET_FROM_DATABASE, UPDATE_BUNS_LABELS, UPDATE_WH_LABELS

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(462, 644)
        self.ui.btn_bins.clicked.connect(self.bin_on_click)
        
    #Gets selected radio btn
    def get_selected(self):
        bins = self.ui.gbRadioButtonsGroup.findChildren(QtWidgets.QRadioButton)       
        for bin in bins:
            if bin.isChecked():
                return bin.text()

    #Updates UI labels
    def update_bin_label(self):
        bins_labels = self.ui.gbRadioButtonsGroup.findChildren(QtWidgets.QLabel)
        for label in bins_labels:
                l = label.objectName()
                per = UPDATE_BUNS_LABELS(str(l[4:]).upper())
                if per != '':
                    label.setText(str(per)+' %')

    #Updates Warehouse labes by calculating Daily KPI needed to archive goals
    def update_daily_wh(self):
        wh_labels = self.ui.groupBox.findChildren(QtWidgets.QLabel)
        for label in wh_labels:
            l = label.objectName()
            per = UPDATE_WH_LABELS(str(l[6:]).upper())
            label.setText(f'{l[6:].upper()} {str(per)}')

    #Simple MSG Box
    def showdialog(self, str):
            QMessageBox.about(self, "Bin's report", str)

    #When Btn is clicked Actions
    def bin_on_click(self):
        #current_day = datetime.date(datetime.now())
        get_bin_input = self.get_selected()
        get_user_input = int(self.ui.imp_bins.text())
        get_user_level = int(self.ui.level.text())
        df = GET_FROM_DATABASE(get_user_input, get_bin_input, get_user_level)
        df.to_excel( f"GENERATED BINS\{get_bin_input}_level{get_user_level}.xlsx", index = False)
        self.showdialog(f"FILE GENERATED")
    
def main():
    app = QApplication(sys.argv)
    win = Main()
    win.show()

    win.update_bin_label()
    win.update_daily_wh()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
