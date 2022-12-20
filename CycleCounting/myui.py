from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(461, 644)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(4)
        Form.setStyleSheet("font: 8pt \"Arial\";")
        self.btn_bins = QtWidgets.QPushButton(Form)
        self.btn_bins.setGeometry(QtCore.QRect(10, 580, 441, 51))
        self.btn_bins.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_bins.setToolTip("")
        self.btn_bins.setToolTipDuration(1)
        self.btn_bins.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Assets/shtyle_sheet.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_bins.setIcon(icon1)
        self.btn_bins.setIconSize(QtCore.QSize(41, 41))
        self.btn_bins.setObjectName("btn_bins")
        self.imp_bins = QtWidgets.QLineEdit(Form)
        self.imp_bins.setGeometry(QtCore.QRect(320, 550, 121, 21))
        self.imp_bins.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.imp_bins.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.imp_bins.setObjectName("imp_bins")
        self.gbRadioButtonsGroup = QtWidgets.QGroupBox(Form)
        self.gbRadioButtonsGroup.setGeometry(QtCore.QRect(10, 20, 291, 551))
        self.gbRadioButtonsGroup.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(225, 225, 225);\n"
"\n"
"")
        self.gbRadioButtonsGroup.setObjectName("gbRadioButtonsGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.gbRadioButtonsGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_c110 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_c110.setText("")
        self.lbl_c110.setObjectName("lbl_c110")
        self.gridLayout.addWidget(self.lbl_c110, 1, 1, 1, 1)
        self.lbl_b110 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b110.setText("")
        self.lbl_b110.setObjectName("lbl_b110")
        self.gridLayout.addWidget(self.lbl_b110, 1, 2, 1, 1)
        self.a100 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a100.setObjectName("a100")
        self.gridLayout.addWidget(self.a100, 0, 0, 1, 1)
        self.b110 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b110.setObjectName("b110")
        self.gridLayout.addWidget(self.b110, 0, 2, 1, 1)
        self.lbl_a110 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a110.setText("")
        self.lbl_a110.setObjectName("lbl_a110")
        self.gridLayout.addWidget(self.lbl_a110, 3, 0, 1, 1)
        self.lbl_a100 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a100.setText("")
        self.lbl_a100.setObjectName("lbl_a100")
        self.gridLayout.addWidget(self.lbl_a100, 1, 0, 1, 1)
        self.c300 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.c300.setObjectName("c300")
        self.gridLayout.addWidget(self.c300, 2, 1, 1, 1)
        self.lbl_c300 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_c300.setText("")
        self.lbl_c300.setObjectName("lbl_c300")
        self.gridLayout.addWidget(self.lbl_c300, 3, 1, 1, 1)
        self.lbl_b300 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b300.setText("")
        self.lbl_b300.setObjectName("lbl_b300")
        self.gridLayout.addWidget(self.lbl_b300, 3, 2, 1, 1)
        self.a300 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a300.setObjectName("a300")
        self.gridLayout.addWidget(self.a300, 4, 0, 1, 1)
        self.c110 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.c110.setObjectName("c110")
        self.gridLayout.addWidget(self.c110, 0, 1, 1, 1)
        self.b300 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b300.setObjectName("b300")
        self.gridLayout.addWidget(self.b300, 2, 2, 1, 1)
        self.c330 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.c330.setObjectName("c330")
        self.gridLayout.addWidget(self.c330, 4, 1, 1, 1)
        self.lbl_a300 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a300.setText("")
        self.lbl_a300.setObjectName("lbl_a300")
        self.gridLayout.addWidget(self.lbl_a300, 5, 0, 1, 1)
        self.a110 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a110.setObjectName("a110")
        self.gridLayout.addWidget(self.a110, 2, 0, 1, 1)
        self.b510 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b510.setObjectName("b510")
        self.gridLayout.addWidget(self.b510, 4, 2, 1, 1)
        self.lbl_a740 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a740.setText("")
        self.lbl_a740.setObjectName("lbl_a740")
        self.gridLayout.addWidget(self.lbl_a740, 25, 0, 1, 1)
        self.lbl_a750 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a750.setText("")
        self.lbl_a750.setObjectName("lbl_a750")
        self.gridLayout.addWidget(self.lbl_a750, 27, 0, 1, 1)
        self.a750 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a750.setObjectName("a750")
        self.gridLayout.addWidget(self.a750, 26, 0, 1, 1)
        self.a710 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a710.setObjectName("a710")
        self.gridLayout.addWidget(self.a710, 18, 0, 1, 1)
        self.lbl_a710 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a710.setText("")
        self.lbl_a710.setObjectName("lbl_a710")
        self.gridLayout.addWidget(self.lbl_a710, 19, 0, 1, 1)
        self.a720 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a720.setObjectName("a720")
        self.gridLayout.addWidget(self.a720, 20, 0, 1, 1)
        self.lbl_a720 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a720.setText("")
        self.lbl_a720.setObjectName("lbl_a720")
        self.gridLayout.addWidget(self.lbl_a720, 21, 0, 1, 1)
        self.lbl_a730 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a730.setText("")
        self.lbl_a730.setObjectName("lbl_a730")
        self.gridLayout.addWidget(self.lbl_a730, 23, 0, 1, 1)
        self.a740 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a740.setObjectName("a740")
        self.gridLayout.addWidget(self.a740, 24, 0, 1, 1)
        self.a730 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a730.setObjectName("a730")
        self.gridLayout.addWidget(self.a730, 22, 0, 1, 1)
        self.lbl_a330 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a330.setText("")
        self.lbl_a330.setObjectName("lbl_a330")
        self.gridLayout.addWidget(self.lbl_a330, 11, 0, 1, 1)
        self.a450 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a450.setObjectName("a450")
        self.gridLayout.addWidget(self.a450, 12, 0, 1, 1)
        self.lbl_a450 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a450.setText("")
        self.lbl_a450.setObjectName("lbl_a450")
        self.gridLayout.addWidget(self.lbl_a450, 13, 0, 1, 1)
        self.lbl_a500 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a500.setText("")
        self.lbl_a500.setObjectName("lbl_a500")
        self.gridLayout.addWidget(self.lbl_a500, 15, 0, 1, 1)
        self.b500 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b500.setObjectName("b500")
        self.gridLayout.addWidget(self.b500, 8, 2, 1, 1)
        self.a510 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a510.setObjectName("a510")
        self.gridLayout.addWidget(self.a510, 16, 0, 1, 1)
        self.lbl_a510 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a510.setText("")
        self.lbl_a510.setObjectName("lbl_a510")
        self.gridLayout.addWidget(self.lbl_a510, 17, 0, 1, 1)
        self.lbl_c330 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_c330.setText("")
        self.lbl_c330.setObjectName("lbl_c330")
        self.gridLayout.addWidget(self.lbl_c330, 5, 1, 1, 1)
        self.lbl_a310 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a310.setText("")
        self.lbl_a310.setObjectName("lbl_a310")
        self.gridLayout.addWidget(self.lbl_a310, 7, 0, 1, 1)
        self.a500 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a500.setObjectName("a500")
        self.gridLayout.addWidget(self.a500, 14, 0, 1, 1)
        self.a320 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a320.setObjectName("a320")
        self.gridLayout.addWidget(self.a320, 8, 0, 1, 1)
        self.a310 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a310.setObjectName("a310")
        self.gridLayout.addWidget(self.a310, 6, 0, 1, 1)
        self.lbl_b510 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b510.setText("")
        self.lbl_b510.setObjectName("lbl_b510")
        self.gridLayout.addWidget(self.lbl_b510, 5, 2, 1, 1)
        self.lbl_b500 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b500.setText("")
        self.lbl_b500.setObjectName("lbl_b500")
        self.gridLayout.addWidget(self.lbl_b500, 9, 2, 1, 1)
        self.lbl_a320 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_a320.setText("")
        self.lbl_a320.setObjectName("lbl_a320")
        self.gridLayout.addWidget(self.lbl_a320, 9, 0, 1, 1)
        self.lbl_b520 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b520.setText("")
        self.lbl_b520.setObjectName("lbl_b520")
        self.gridLayout.addWidget(self.lbl_b520, 7, 2, 1, 1)
        self.a330 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.a330.setObjectName("a330")
        self.gridLayout.addWidget(self.a330, 10, 0, 1, 1)
        self.b520 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b520.setObjectName("b520")
        self.gridLayout.addWidget(self.b520, 6, 2, 1, 1)
        self.b750 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b750.setObjectName("b750")
        self.gridLayout.addWidget(self.b750, 10, 2, 1, 1)
        self.lbl_b750 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b750.setText("")
        self.lbl_b750.setObjectName("lbl_b750")
        self.gridLayout.addWidget(self.lbl_b750, 11, 2, 1, 1)
        self.b230 = QtWidgets.QRadioButton(self.gbRadioButtonsGroup)
        self.b230.setObjectName("b230")
        self.gridLayout.addWidget(self.b230, 12, 2, 1, 1)
        self.lbl_b230 = QtWidgets.QLabel(self.gbRadioButtonsGroup)
        self.lbl_b230.setText("")
        self.lbl_b230.setObjectName("lbl_b230")
        self.gridLayout.addWidget(self.lbl_b230, 13, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(310, 40, 141, 501))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 121, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_MKI = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_MKI.setScaledContents(False)
        self.label_MKI.setObjectName("label_MKI")
        self.verticalLayout.addWidget(self.label_MKI, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_JTS1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_JTS1.setObjectName("label_JTS1")
        self.verticalLayout.addWidget(self.label_JTS1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_JTS2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_JTS2.setObjectName("label_JTS2")
        self.verticalLayout.addWidget(self.label_JTS2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.level = QtWidgets.QSpinBox(Form)
        self.level.setGeometry(QtCore.QRect(320, 10, 121, 21))
        self.level.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.level.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.level.setObjectName("level")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 311, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CycleCount"))
        self.btn_bins.setText(_translate("Form", "Generate Bin\'s .xlsx file"))
        self.imp_bins.setText(_translate("Form", "0"))
        self.a100.setText(_translate("Form", "A100"))
        self.b110.setText(_translate("Form", "B110"))
        self.c300.setText(_translate("Form", "C300"))
        self.a300.setText(_translate("Form", "A300"))
        self.c110.setText(_translate("Form", "C110"))
        self.b300.setText(_translate("Form", "B300"))
        self.c330.setText(_translate("Form", "C330"))
        self.a110.setText(_translate("Form", "A110"))
        self.b510.setText(_translate("Form", "B510"))
        self.a750.setText(_translate("Form", "A750"))
        self.a710.setText(_translate("Form", "A710"))
        self.a720.setText(_translate("Form", "A720"))
        self.a740.setText(_translate("Form", "A740"))
        self.a730.setText(_translate("Form", "A730"))
        self.a450.setText(_translate("Form", "A450"))
        self.b500.setText(_translate("Form", "B500"))
        self.a510.setText(_translate("Form", "A510"))
        self.a500.setText(_translate("Form", "A500"))
        self.a320.setText(_translate("Form", "A320"))
        self.a310.setText(_translate("Form", "A310"))
        self.a330.setText(_translate("Form", "A330"))
        self.b520.setText(_translate("Form", "B520"))
        self.b750.setText(_translate("Form", "B750"))
        self.b230.setText(_translate("Form", "B230"))
        self.groupBox.setTitle(_translate("Form", "To Count Daily"))
        self.label_MKI.setText(_translate("Form", "MKI"))
        self.label_JTS1.setText(_translate("Form", "JTS1"))
        self.label_JTS2.setText(_translate("Form", "JTS2"))
        self.label.setText(_translate("Form", "MKI"))
        self.label_2.setText(_translate("Form", "JTS1"))
        self.label_3.setText(_translate("Form", "JTS2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())