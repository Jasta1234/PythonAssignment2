import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from controller import *


class Person:
    def __init__(self, first_name, last_name, phone_number, email, age, gender, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email
        self.__age = age
        self.__gender = gender
        self.__address = address

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def address(self):
        return self.__address


class Doctor(Person):
    def __init__(self, first_name, last_name, phone_number, email, age, gender, address, specialization,
                 years_of_experience, doctor_id):
        self.__specialization = specialization
        self.__years_of_experience = years_of_experience
        self.__doctor_id = doctor_id
        Person.__init__(self, first_name, last_name, phone_number, email, age, gender, address)

    @property
    def specialization(self):
        return self.__specialization

    @property
    def experience(self):
        return self.__years_of_experience

    @property
    def doctor_id(self):
        return self.__doctor_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home-ui.ui', self)

        self.initializeAddDoctorWidgets()
        self.initializeEditDeleteDoctorWidgets()

    def initializeAddDoctorWidgets(self):
        self.lineEditFirstName = self.findChild(QLineEdit, 'lineEditFirstName')
        self.lineEditLastName = self.findChild(QLineEdit, 'lineEditLastName')
        self.lineEditPhoneNumber = self.findChild(QLineEdit, 'lineEditPhoneNumber')
        self.lineEditEmail = self.findChild(QLineEdit, 'lineEditEmail')
        self.lineEditAge = self.findChild(QLineEdit, 'lineEditAge')
        self.lineEditSpecilization = self.findChild(QLineEdit, 'lineEditSpecilization')
        self.lineEditAddress = self.findChild(QLineEdit, 'lineEditAddress')
        self.lineEditYearsOfExperience = self.findChild(QLineEdit, 'lineEditYearsOfExperience')
        self.cboGender = self.findChild(QComboBox, 'cboGender')
        self.btnAddDoctor = self.findChild(QPushButton, 'btnAddDoctor')
        self.lblDoctorFeedback = self.findChild(QLabel, 'lblDoctorFeedback')
        self.btnAddDoctor.clicked.connect(self.btnAddDoctorClickHandler)

    def initializeEditDeleteDoctorWidgets(self):
        self.cboDoctor = self.findChild(QComboBox, 'cboDoctor')
        self.cboDocId = self.findChild(QComboBox, 'cboDocId')
        self.lineEditFName = self.findChild(QLineEdit, 'lineEditFName')
        self.lineEditLName = self.findChild(QLineEdit, 'lineEditLName')
        self.lineEditPNumber = self.findChild(QLineEdit, 'lineEditPNumber')
        self.lineEditEmail_2 = self.findChild(QLineEdit, 'lineEditEmail_2')
        self.cboGender_2 = self.findChild(QComboBox, 'cboGender_2')
        self.lineEditAge_2 = self.findChild(QLineEdit, 'lineEditAge_2')
        self.lineEditAddr = self.findChild(QLineEdit, 'lineEditAddr')
        self.lineEditSpec = self.findChild(QLineEdit, 'lineEditSpec')
        self.lineEditYoe = self.findChild(QLineEdit, 'lineEditYoe')
        self.btnEditDoctor = self.findChild(QPushButton, 'btnEditDoctor')
        self.btnDeleteDoctor = self.findChild(QPushButton, 'btnDeleteDoctor')
        self.lblModifyDoctor = self.findChild(QLabel, 'lblModifyDoctor')
        self.btnDeleteDoctor.clicked.connect(self.btnDeleteDoctorClickedHandler)
        self.btnEditDoctor.clicked.connect(self.btnUpdateDoctorClickHandler)

        colNames, rows = getDoctorIdsAndNames()
        print(colNames, rows)
        for row in rows:
            self.cboDoctor.addItem(row[1], userData=row[0])
        self.cboDoctor.currentIndexChanged.connect(self.cboDoctorCurrentIndexChangedHandler)

        self.refreshDoctorComboBox()

    def btnDeleteDoctorClickedHandler(self):
        try:
            fname = self.lineEditFName.text()
            lname = self.lineEditLName.text()

            msg = QMessageBox(self)
            msg.setWindowTitle("Delete Confirmation")
            msg.setText(f"Are you sure you want to delete {fname} {lname}")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
            if button == QMessageBox.StandardButton.Yes:
                did = self.cboDoctor.currentData()
                result = deleteDoctorById(did)
                if result == 1:
                    self.lblModifyDoctor.setText('Success')
                    self.refreshUpdateDoctorTab()
                else:
                    self.lblModifyDoctor.setText('Failure')
            elif button == QMessageBox.StandardButton.No:
                self.lblModifyDoctor.setText('Delete Cancelled')
        except Exception as e:
            self.lblModifyDoctor.setText(e)

        self.refreshDoctorComboBox()

    def btnUpdateDoctorClickHandler(self):
        did = self.cboDoctor.currentData()
        fname = self.lineEditFName.text()
        lname = self.lineEditLName.text()
        email = self.lineEditEmail_2.text()
        gend = self.cboGender_2.currentText()
        pnumber = self.lineEditPNumber.text()
        age = self.lineEditAge_2.text()
        addr = self.lineEditAddr.text()
        spec = self.lineEditSpec.text()
        yoe = self.lineEditYoe.text()
        result = updateDoctor(did, fname, lname, gend, pnumber, email, age, addr, spec, yoe)
        index = self.cboDocId.currentIndex()
        if result == 1:
            self.lblModifyDoctor.setText('Success')
        else:
            self.lblModifyDoctor.setText('Failure')
        self.refreshUpdateDoctorTab()
        self.cboDocId.setCurrentIndex(index)

    def cboDoctorCurrentIndexChangedHandler(self):
        self.refreshDoctorComboBox()

    def refreshDoctorComboBox(self):
        try:
            docId = self.cboDoctor.currentData()
            info = getDoctorInfoById(docId)
            print("info", info)
            self.cboDocId.addItem(str(info['did']))
            self.lineEditFName.setText(info['fname'])
            self.lineEditLName.setText(info['lname'])
            self.lineEditPNumber.setText(info['pnumber'])
            self.lineEditEmail_2.setText(info['email'])
            self.cboGender_2.addItem(info['gender'])
            self.cboGender_2.addItem('Male')
            self.cboGender_2.addItem('Female')
            self.cboGender_2.addItem('Other')
            self.lineEditAge_2.setText(str(info['age']))
            self.lineEditAddr.setText(info['address'])
            self.lineEditSpec.setText(info['spec'])
            self.lineEditYoe.setText(str(info['yoe']))
        except Exception as e:
            print(e)

    def refreshUpdateDoctorTab(self):
        colNames, rows = getDoctorIdsAndNames()
        print(colNames, rows)
        self.cboDoctor.clear()
        self.cboGender.clear()
        self.cboDocId.clear()

        for row in rows:
            self.cboDoctor.addItem(row[1], userData=row[0])
        self.cboDoctor.currentIndexChanged.connect(self.cboDoctorCurrentIndexChangedHandler)

    def btnAddDoctorClickHandler(self):
        try:
            fname = self.lineEditFirstName.text()
            assert fname != '', 'First name is mandatory.'
            lname = self.lineEditLastName.text()
            assert lname != '', 'Last name is mandatory.'
            pnumber = self.lineEditPhoneNumber.text()
            assert pnumber != '', 'Phone number is mandatory.'
            email = self.lineEditEmail.text()
            assert email != '', 'Email is mandatory.'
            age = self.lineEditAge.text()
            assert age != '', 'Age is mandatory.'
            spec = self.lineEditSpecilization.text()
            assert spec != '', 'Specilization is mandatory.'
            addr = self.lineEditAddress.text()
            assert addr != '', 'Address is mandatory.'
            yoe = self.lineEditYearsOfExperience.text()
            assert yoe != '', 'Years of experience is mandatory.'
            gend = self.cboGender.currentText()
            assert gend != 'Select', 'Please select a gender.'

            result = add_doctor(fname, lname, gend, pnumber, email, age, addr, spec, yoe)

        except Exception as e:
            self.lblDoctorFeedback.setText(str(e))

        else:
            if result == 1:
                self.lblDoctorFeedback.setText("Student Added")
            else:
                self.lblDoctorFeedback.setText("Student could not be added")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
