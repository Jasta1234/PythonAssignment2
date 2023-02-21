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

    def btnAddDoctorClickHandler(self):
        try:
            fname = self.lineEditFirstName.text()
            assert fname != '', 'First name is mandatory'
            lname = self.lineEditLastName.text()
            assert lname != '', 'Last name is mandatory'
            pnumber = self.lineEditPhoneNumber.text()
            email = self.lineEditEmail.text()
            assert email != '', 'Email is mandatory'
            age = self.lineEditAge.text()
            assert age != '', 'Age is mandatory'
            assert age != int, 'Age has to be an integer.'
            specilization = self.lineEditSpecilization.text()
            assert specilization != '', 'Specilization is mandatory'
            gender = self.cboGender.currentData()
            assert gender != 'Select', 'Please select a gender...'
            assert gender != '', 'Gender is mandatory'
            address = self.lineEditAddress.text()
            assert address != '', 'Address is mandatory'
            yearsofexperience = self.lineEditYearsOfExperience.text()
            assert yearsofexperience != int, 'Years of experience has to be an integer.'
            assert yearsofexperience != '', 'years of experience is mandatory'
            result = add_doctor(fname, lname, gender, pnumber, email, int(age), address, specilization,
                                int(yearsofexperience))
        except Exception as e:
            self.lblDoctorFeedback.setText(str(e))
            print(e)
        else:
            if result == 1:
                self.lblDoctorFeedback.setText("Doctor added")
            else:
                self.lblDoctorFeedback.setText("Error adding doctor")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
