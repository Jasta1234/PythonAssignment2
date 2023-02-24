from mysql_functions import *

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
    print('stuinfo', docInfo)
    data = {'did': docInfo[0], 'fname': docInfo[1], 'lname': docInfo[2], 'gender': docInfo[3], 'pnumber': docInfo[4],
            'email': docInfo[5], 'age': docInfo[6], 'address': docInfo[7], 'spec': docInfo[8], 'yoe': docInfo[9]}
    print(data)
    return data

def getPatientInfoById(patId):
    """
    SQL code to get the information of a doctor given a doctor ID
    """
    sql = f"SELECT * FROM doctors_management_system.patients where patient_id = {patId}; "
    patInfo = executeQueryAndReturnResult(sql)[1][0]
    print('stuinfo', patInfo)
    data = {'pid': patInfo[0], 'fname': patInfo[1], 'lname': patInfo[2], 'gender': patInfo[3], 'pnumber': patInfo[4],
            'email': patInfo[5], 'age': patInfo[6], 'address': patInfo[7]}
    print(data)
    return data


def getDoctorIdsAndNames():
    """
    SQL code to get doctor ID's and names
    """
    sql = f"SELECT doctor_id, concat(first_name, ' ', last_name) as 'Doctor Name' FROM doctors_management_system.doctors;"
    return executeQueryAndReturnResult(sql)

def getPatientIdsAndNames():
    """
    SQL code to get patient ID's and names
    """
    sql = f"SELECT patient_id, concat(first_name, ' ', last_name) as 'Patient Name' FROM doctors_management_system.patients;"
    return executeQueryAndReturnResult(sql)

def deleteDoctorById(did):
    """
    SQL code delete a doctor by ID
    """
    sql = f"DELETE FROM `doctors_management_system`.`doctors` WHERE (`doctor_id` = '{did}');"
    return executeQueryAndCommit(sql)

def deletePatientById(pid):
    """
    SQL code delete a doctor by ID
    """
    sql = f"DELETE FROM `doctors_management_system`.`patients` WHERE (`patient_id` = '{pid}');"
    return executeQueryAndCommit(sql)


def updateDoctor(did, fname, lname, gend, pnumber, email, age, addr, spec, yoe):
    """
    SQL code to update a doctor
    """
    sql = f"UPDATE `doctors_management_system`.`doctors` SET `first_name` = '{fname}', `last_name` = '{lname}', `gender` = '{gend}', `phone_number` = '{pnumber}', `email` = '{email}', `age` = '{age}', `address` = '{addr}', `specilization` = '{spec}', `years_of_experience` = '{yoe}' WHERE (`doctor_id` = {did});"
    return executeQueryAndCommit(sql)

def updatePatient(pid, fname, lname, gend, pnumber, email, age, addr):
    """
    SQL code to update a patient
    """
    sql = f"UPDATE `doctors_management_system`.`patients` SET `first_name` = '{fname}', `last_name` = '{lname}', `gender` = '{gend}', `phone_number` = '{pnumber}', `email` = '{email}', `age` = '{age}', `address` = '{addr}' WHERE (`patient_id` = {pid});"
    return executeQueryAndCommit(sql)


def getAllDoctors():
    """
    SQL code to get all doctors
    """
    sql = "SELECT * FROM `doctors_management_system`.`doctors`;"
    return executeQueryAndReturnResult(sql)


def addPatient(fname, lname, gend, pnumber, email, age, addr):
    sql = f"INSERT INTO `doctors_management_system`.`patients`(`first_name`, `last_name`, `gender`, `phone_number`, `email`, `age`, `address`) VALUES('{fname}', '{lname}', '{gend}', '{pnumber}', '{email}', {age}, '{addr}');"
    return executeQueryAndCommit(sql)


def getAllPatients():
    sql = "SELECT * FROM `doctors_management_system`.`patients`;"
    return executeQueryAndReturnResult(sql)