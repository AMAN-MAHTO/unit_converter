# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\unit_converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import length_conv
import pressure_conv
import temp_conv


class Ui_Unit_Convertor(object):
    def setupUi(self, Unit_Convertor):
        Unit_Convertor.setObjectName("Unit_Convertor")
        Unit_Convertor.resize(400, 268)
        self.convertions = QtWidgets.QComboBox(Unit_Convertor)
        self.convertions.setGeometry(QtCore.QRect(10, 50, 371, 22))
        self.convertions.setObjectName("convertions")

        self.second_unit = QtWidgets.QComboBox(Unit_Convertor)
        self.second_unit.setGeometry(QtCore.QRect(220, 160, 161, 22))
        self.second_unit.setObjectName("second_unit")

        self.first_unit = QtWidgets.QComboBox(Unit_Convertor)
        self.first_unit.setGeometry(QtCore.QRect(10, 160, 161, 22))
        self.first_unit.setObjectName("first_unit")

        self.input = QtWidgets.QLineEdit(Unit_Convertor)
        self.input.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Potta One")
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setObjectName("input")

        self.output = QtWidgets.QLineEdit(Unit_Convertor)
        self.output.setGeometry(QtCore.QRect(220, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Potta One")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setObjectName("output")

        self.label = QtWidgets.QLabel(Unit_Convertor)
        self.label.setGeometry(QtCore.QRect(180, 110, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.Button = QtWidgets.QPushButton(Unit_Convertor)
        self.Button.setGeometry(QtCore.QRect(280, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Potta One")
        font.setPointSize(12)
        self.Button.setFont(font)
        self.Button.setObjectName("Button")

        self.label_2 = QtWidgets.QLabel(Unit_Convertor)
        self.label_2.setGeometry(QtCore.QRect(16, 9, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Potta One")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Unit_Convertor)
        QtCore.QMetaObject.connectSlotsByName(Unit_Convertor)

        # code added
        self.Button.clicked.connect(self.button_click)
        self.convertions.addItems(['Length','Pressure','Temprature'])
        self.update_first_and_second_units_combobox()
        self.convertions.currentTextChanged.connect(self.update_first_and_second_units_combobox)
    
    def update_first_and_second_units_combobox(self):
        self.first_unit.clear()
        self.second_unit.clear()
        if self.convertions.currentText() == 'Length':
            self.first_unit.addItems(length_conv.list_of_lenths_units())
            self.second_unit.addItems(length_conv.list_of_lenths_units())
        elif self.convertions.currentText() == 'Pressure':
            self.first_unit.addItems(pressure_conv.list_of_pressure_units())
            self.second_unit.addItems(pressure_conv.list_of_pressure_units())
        elif self.convertions.currentText() == 'Temprature':
            self.first_unit.addItems(temp_conv.list_of_temp_units())
            self.second_unit.addItems(temp_conv.list_of_temp_units())

    def output(self,ans):
        self.output.clear()
        self.output.setText(str(round(ans,7)))

    def button_click(self):
        num=float(self.input.text())
        first_unit = self.first_unit.currentText()
        second_unit = self.second_unit.currentText()
        convertion_type = self.convertions.currentText()

        if convertion_type == 'Length':
            ans = length_conv.length(num,first_unit,second_unit)
            
        elif convertion_type == 'Pressure':
            ans = pressure_conv.pressure(num,first_unit,second_unit)

        elif convertion_type== 'Temprature':
            ans = temp_conv.temp(num,first_unit,second_unit)
            

    def retranslateUi(self, Unit_Convertor):
        _translate = QtCore.QCoreApplication.translate
        Unit_Convertor.setWindowTitle(_translate("Unit_Convertor", "Form"))
        self.label.setText(_translate("Unit_Convertor", "="))
        self.Button.setText(_translate("Unit_Convertor", "Convert"))
        self.label_2.setText(_translate("Unit_Convertor", "Unit Conveter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Unit_Convertor = QtWidgets.QWidget()
    ui = Ui_Unit_Convertor()
    ui.setupUi(Unit_Convertor)
    Unit_Convertor.show()
    sys.exit(app.exec_())
