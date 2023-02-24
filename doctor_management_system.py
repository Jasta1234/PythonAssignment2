import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from controller import *

class Person:
    """
    Class of a person
    """

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
    """
    Class of a doctor
    """

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
    """
    MainWindow class for the PyQt6 program
    """

    def __init__(self):
        super().__init__()
        uic.loadUi('home-ui.ui', self)

        self.initializeAddDoctorWidgets()
        self.initializeEditDeleteDoctorWidgets()
        self.initializeAllDoctorTbl()
        self.initializeAddPatientWidgets()
        self.initializeAllPatientTbl()
        self.initializeEditDeletePatientWidgets()

    def initializeAddPatientWidgets(self):
        """
        Code to initialize the add doctor widgets
        """
        self.lineEditFirstName_2 = self.findChild(QLineEdit, 'lineEditFirstName_2')
        self.lineEditLastName_2 = self.findChild(QLineEdit, 'lineEditLastName_2')
        self.lineEditPhoneNumber_2 = self.findChild(QLineEdit, 'lineEditPhoneNumber_2')
        self.lineEditEmail_3 = self.findChild(QLineEdit, 'lineEditEmail_3')
        self.lineEditAge_3 = self.findChild(QLineEdit, 'lineEditAge_3')
        self.lineEditAddress_2 = self.findChild(QLineEdit, 'lineEditAddress_2')
        self.cboGender_3 = self.findChild(QComboBox, 'cboGender_3')
        self.btnAddPatient_2 = self.findChild(QPushButton, 'btnAddPatient_2')
        self.lblPatientFeedback = self.findChild(QLabel, 'lblPatientFeedback')
        self.btnAddPatient_2.clicked.connect(self.btnAddPatientClickHandler)

    def initializeAddDoctorWidgets(self):
        """
        Code to initialize the add doctor widgets
        """
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

    def initializeAllDoctorTbl(self):
        """
        Code to initialize the table that contains all doctors
        """
        self.tblAllDoctors = self.findChild(QTableWidget, 'tblAllDoctors')
        colNames, data = getAllDoctors()
        self.displayTableData(colNames, data, self.tblAllDoctors)

    def initializeAllPatientTbl(self):
        """
        Code to initialize the table that contains all patients
        """
        self.tblAllPatients = self.findChild(QTableWidget, 'tblAllPatients')
        colNames, data = getAllPatients()
        self.displayPatientInTable(colNames, data, self.tblAllPatients)

    def refreshAllTabs(self):
        """
        Code to refresh all tables/tabs
        """
        self.refreshAllDoctorTbl()
        self.refreshUpdateDoctorTab()

    def initializeEditDeleteDoctorWidgets(self):
        """
        Code to initialize the edit/delete doctor widgets
        """
        self.cboDoctor = self.findChild(QComboBox, 'cboDoctor')
        self.lineEditDocId = self.findChild(QLineEdit, 'lineEditDocId')
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

    def initializeEditDeletePatientWidgets(self):
        """
        Code to initialize the edit/delete doctor widgets
        """
        self.cboPatient = self.findChild(QComboBox, 'cboPatient')
        self.lineEditPatientId = self.findChild(QLineEdit, 'lineEditPatientId')
        self.lineEditFName_2 = self.findChild(QLineEdit, 'lineEditFName_2')
        self.lineEditLName_2 = self.findChild(QLineEdit, 'lineEditLName_2')
        self.lineEditPNumber_2 = self.findChild(QLineEdit, 'lineEditPNumber_2')
        self.lineEditEmail_4 = self.findChild(QLineEdit, 'lineEditEmail_4')
        self.cboGender_4 = self.findChild(QComboBox, 'cboGender_4')
        self.lineEditAge_4 = self.findChild(QLineEdit, 'lineEditAge_4')
        self.lineEditAddr_2 = self.findChild(QLineEdit, 'lineEditAddr_2')
        self.btnEditPatient = self.findChild(QPushButton, 'btnEditPatient')
        self.btnDeletePatient = self.findChild(QPushButton, 'btnDeletePatient')
        self.lblModifyPatient = self.findChild(QLabel, 'lblModifyPatient')
        self.btnDeletePatient.clicked.connect(self.btnDeletePatientClickedHandler)
        self.btnEditPatient.clicked.connect(self.btnUpdatePatientClickHandler)

        colNames, rows = getPatientIdsAndNames()
        print(colNames, rows)
        for row in rows:
            self.cboPatient.addItem(row[1], userData=row[0])
        self.cboPatient.currentIndexChanged.connect(self.cboPatientCurrentIndexChangedHandler)

        self.refreshPatientComboBox()

    def btnDeletePatientClickedHandler(self):
        """
        Button delete clicked handler
        """
        try:
            fname = self.lineEditFName_2.text()
            lname = self.lineEditLName_2.text()

            msg = QMessageBox(self)
            msg.setWindowTitle("Delete Confirmation")
            msg.setText(f"Are you sure you want to delete {fname} {lname}")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
            if button == QMessageBox.StandardButton.Yes:
                pid = self.cboPatient.currentData()
                result = deletePatientById(pid)
                if result == 1:
                    self.lblModifyPatient.setText('Success')
                    self.refreshAllPatientTabs()
                else:
                    self.lblModifyPatient.setText('Failure')
            elif button == QMessageBox.StandardButton.No:
                self.lblModifyPatient.setText('Delete Cancelled')
        except Exception as e:
            self.lblModifyPatient.setText(e)


    def btnDeleteDoctorClickedHandler(self):
        """
        Button delete clicked handler
        """
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
                    self.refreshAllTabs()
                else:
                    self.lblModifyDoctor.setText('Failure')
            elif button == QMessageBox.StandardButton.No:
                self.lblModifyDoctor.setText('Delete Cancelled')
        except Exception as e:
            self.lblModifyDoctor.setText(e)



    def btnUpdateDoctorClickHandler(self):
        """
        Button update clicked handler
        """
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
        index = self.cboDoctor.currentIndex()
        if result == 1:
            self.lblModifyDoctor.setText('Success')
            self.refreshAllTabs()
            self.cboDoctor.setCurrentIndex(index)
        else:
            self.lblModifyDoctor.setText('Failure')

    def btnUpdatePatientClickHandler(self):
        """
        Button update clicked handler
        """
        pid = self.cboPatient.currentData()
        fname = self.lineEditFName_2.text()
        lname = self.lineEditLName_2.text()
        pnumber = self.lineEditPNumber_2.text()
        email = self.lineEditEmail_4.text()
        gend = self.cboGender_4.currentText()
        age = self.lineEditAge_4.text()
        addr = self.lineEditAddr_2.text()
        result = updatePatient(pid, fname, lname, gend, pnumber, email, age, addr)
        index = self.cboPatient.currentIndex()
        if result == 1:
            self.lblModifyPatient.setText('Success')
            self.refreshAllPatientTabs()
            self.cboPatient.setCurrentIndex(index)
        else:
            self.lblModifyPatient.setText('Failure')

    def cboDoctorCurrentIndexChangedHandler(self):
        """
        Refreshes the Doctor combo box if the index is changed
        """
        self.refreshDoctorComboBox()

    def refreshDoctorComboBox(self):
        """
        Code to refresh the doctor combo box
        """
        try:
            docId = self.cboDoctor.currentData()
            info = getDoctorInfoById(docId)
            print("info", info)
            self.lineEditDocId.setText(str(info['did']))
            self.lineEditFName.setText(info['fname'])
            self.lineEditLName.setText(info['lname'])
            self.lineEditPNumber.setText(info['pnumber'])
            self.lineEditEmail_2.setText(info['email'])
            self.cboGender_2.setCurrentText(info['gender'])
            self.lineEditAge_2.setText(str(info['age']))
            self.lineEditAddr.setText(info['address'])
            self.lineEditSpec.setText(info['spec'])
            self.lineEditYoe.setText(str(info['yoe']))
        except Exception as e:
            print(e)

    def refreshPatientComboBox(self):
        """
        Code to refresh the doctor combo box
        """
        try:
            patId = self.cboPatient.currentData()
            info = getPatientInfoById(patId)
            print("info", info)
            self.lineEditPatientId.setText(str(info['pid']))
            self.lineEditFName_2.setText(info['fname'])
            self.lineEditLName_2.setText(info['lname'])
            self.lineEditPNumber_2.setText(info['pnumber'])
            self.lineEditEmail_4.setText(info['email'])
            self.cboGender_4.setCurrentText(info['gender'])
            self.lineEditAge_4.setText(str(info['age']))
            self.lineEditAddr_2.setText(info['address'])
        except Exception as e:
            print(e)

    def refreshUpdateDoctorTab(self):
        """
        Code to refresh the update doctor tab
        """
        colNames, rows = getDoctorIdsAndNames()
        print(colNames, rows)
        self.cboDoctor.clear()

        for row in rows:
            self.cboDoctor.addItem(row[1], userData=row[0])
        self.cboDoctor.currentIndexChanged.connect(self.cboDoctorCurrentIndexChangedHandler)

    def refreshAllPatientTabs(self):
        """
        Code to refresh all tables/tabs
        """
        self.refreshAllPatientTbl()
        self.refreshUpdatePatientTab()

    def refreshUpdatePatientTab(self):
        """
        Code to refresh the update patient tab
        """
        colNames, rows = getPatientIdsAndNames()
        print(colNames, rows)
        self.cboPatient.clear()

        for row in rows:
            self.cboPatient.addItem(row[1], userData=row[0])
        self.cboPatient.currentIndexChanged.connect(self.cboPatientCurrentIndexChangedHandler)

    def cboPatientCurrentIndexChangedHandler(self):
        self.refreshPatientComboBox()

    def btnAddDoctorClickHandler(self):
        """
        Button add doctor click handler
        """
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
                self.lblDoctorFeedback.setText("Doctor Added")
                self.refreshAllTabs()
                self.refreshDoctorComboBox()
                self.lineEditFirstName.clear()
                self.lineEditLastName.clear()
                self.lineEditPhoneNumber.clear()
                self.lineEditEmail.clear()
                self.lineEditAge.clear()
                self.lineEditSpecilization.clear()
                self.lineEditAddress.clear()
                self.lineEditYearsOfExperience.clear()
                self.cboGender.setCurrentText('Select')

            else:
                self.lblDoctorFeedback.setText("Doctor could not be added")

    def displayTableData(self, columns, rows, table: QTableWidget):
        """
        Code to display all the data of doctors in a table
        """
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):  # once for each row
            row = rows[i]
            for j in range(len(row)):  # once for each cell in a given row
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['Doctor ID', 'First name', 'Last name', 'Gender', 'Phone number', 'Email', 'Age', 'Address',
                   'Specilization', 'Years of experience']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def refreshAllDoctorTbl(self):
        """
        Code to refresh the doctors table
        """
        colNames, data = getAllDoctors()
        self.displayTableData(colNames, data, self.tblAllDoctors)

    def displayPatientInTable(self, columns, rows, table: QTableWidget):
        """
        Code to display all the data of patients in a table
        """
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ["Patient ID", "First name", "Last name", "Gender", "Phone Number", "Email", "Age", "Address"]
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def refreshAllPatientTbl(self):
        """
        Code to refresh the patients table
        """
        colNames, data = getAllPatients()
        self.displayPatientInTable(colNames, data, self.tblAllPatients)

    def btnAddPatientClickHandler(self):
        """
        Button add patient click handler
        """
        try:
            fname = self.lineEditFirstName_2.text()
            assert fname != '', 'First name is mandatory.'
            lname = self.lineEditLastName_2.text()
            assert lname != '', 'Last name is mandatory.'
            pnumber = self.lineEditPhoneNumber_2.text()
            assert pnumber != '', 'Phone number is mandatory.'
            email = self.lineEditEmail_3.text()
            assert email != '', 'Email is mandatory.'
            age = self.lineEditAge_3.text()
            assert age != '', 'Age is mandatory.'
            addr = self.lineEditAddress_2.text()
            assert addr != '', 'Address is mandatory.'
            gend = self.cboGender_3.currentText()
            assert gend != 'Select', 'Please select a gender.'

            result = addPatient(fname, lname, gend, pnumber, email, age, addr)

        except Exception as e:
            self.lblPatientFeedback.setText(str(e))

        else:
            if result == 1:
                self.lblPatientFeedback.setText("Patient Added")
                self.refreshAllPatientTabs()
                self.refreshPatientComboBox()
                self.lineEditFirstName_2.clear()
                self.lineEditLastName_2.clear()
                self.lineEditPhoneNumber_2.clear()
                self.lineEditEmail_3.clear()
                self.lineEditAge_3.clear()
                self.lineEditAddress_2.clear()
                self.cboGender_3.clear()
            else:
                self.lblPatientFeedback.setText("Patient could not be added")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
