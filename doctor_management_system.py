import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
import mysql.connector


def executeQueryAndReturnResult(query, host='localhost', username='root', password='root', port=3306,
                                database='doctors_management_system'):
    """
    :returns the results of an SQL query
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.column_names, cursor.fetchall()


def executeQueryAndCommit(query, host='localhost', username='root', password='root', port=3306,
                          database='doctors_management_system'):
    """
    executes and commits an SQL query
    """
    with mysql.connector.connect(host=host, user=username, password=password, port=port, database=database) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount




#Controller Code
def add_doctor(fname, lname, gend, pnumber, email, age, addr, spec, yoe):
    """
    SQL code to add a doctor
    """
    sql = f"INSERT INTO `doctors_management_system`.`doctors`(`first_name`, `last_name`, `gender`, `phone_number`, `email`, `age`, `address`, `specilization`, `years_of_experience`) VALUES('{fname}', '{lname}', '{gend}', '{pnumber}', '{email}', {age}, '{addr}', '{spec}', {yoe});"
    return executeQueryAndCommit(sql)

def getDoctorInfoById(docId):
    """
    SQL code to get the information of a doctor given a doctor ID
    """
    sql = f"SELECT * FROM doctors_management_system.doctors where doctor_id = {docId}; "
    docInfo = executeQueryAndReturnResult(sql)[1][0]
    print('stuinfo',docInfo)
    data = {'did': docInfo[0], 'fname': docInfo[1], 'lname': docInfo[2], 'gender': docInfo[3], 'pnumber': docInfo[4], 'email': docInfo[5], 'age': docInfo[6], 'address': docInfo[7], 'spec': docInfo[8], 'yoe': docInfo[9]}
    print(data)
    return data

def getDoctorIdsAndNames():
    """
    SQL code to get doctor ID's and names
    """
    sql =f"SELECT doctor_id, concat(first_name, ' ', last_name) as 'Doctor Name' FROM doctors_management_system.doctors;"
    return executeQueryAndReturnResult(sql)

def deleteDoctorById(did):
    """
    SQL code delete a doctor by ID
    """
    sql = f"DELETE FROM `doctors_management_system`.`doctors` WHERE (`doctor_id` = '{did}');"
    return executeQueryAndCommit(sql)

def updateDoctor(did, fname, lname, gend, pnumber, email, age, addr, spec, yoe):
    """
    SQL code to update a doctor
    """
    sql = f"UPDATE `doctors_management_system`.`doctors` SET `first_name` = '{fname}', `last_name` = '{lname}', `gender` = '{gend}', `phone_number` = '{pnumber}', `email` = '{email}', `age` = '{age}', `address` = '{addr}', `specilization` = '{spec}', `years_of_experience` = '{yoe}' WHERE (`doctor_id` = {did});"
    return executeQueryAndCommit(sql)

def getAllDoctors():
    """
    SQL code to get all doctors
    """
    sql = "SELECT * FROM `doctors_management_system`.`doctors`;"
    return executeQueryAndReturnResult(sql)


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

        self.refreshDoctorComboBox()

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
        index = self.cboDocId.currentIndex()
        if result == 1:
            self.lblModifyDoctor.setText('Success')
        else:
            self.lblModifyDoctor.setText('Failure')
        self.refreshAllTabs()
        self.cboDocId.setCurrentIndex(index)

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

    def refreshUpdateDoctorTab(self):
        """
        Code to refresh the update doctor tab
        """
        colNames, rows = getDoctorIdsAndNames()
        print(colNames, rows)
        self.cboDoctor.clear()
        self.cboGender.clear()
        self.cboDocId.clear()

        for row in rows:
            self.cboDoctor.addItem(row[1], userData=row[0])
        self.cboDoctor.currentIndexChanged.connect(self.cboDoctorCurrentIndexChangedHandler)

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
                self.lblDoctorFeedback.setText("Student Added")
                self.refreshAllTabs()
                self.refreshDoctorComboBox()
            else:
                self.lblDoctorFeedback.setText("Student could not be added")

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
        columns = ['Doctor ID', 'First name', 'Last name', 'Gender', 'Phone number', 'Email', 'Age', 'Address', 'Specilization', 'Years of experience']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def refreshAllDoctorTbl(self):
        """
        Code to refresh the doctors table
        """
        colNames, data = getAllDoctors()
        self.displayTableData(colNames, data, self.tblAllDoctors)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
