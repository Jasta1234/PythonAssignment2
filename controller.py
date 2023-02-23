from mysql_functions import *

def add_doctor(fname, lname, gend, pnumber, email, age, addr, spec, yoe):
    sql = f"INSERT INTO `doctors_management_system`.`doctors`(`first_name`, `last_name`, `gender`, `phone_number`, `email`, `age`, `address`, `specilization`, `years_of_experience`) VALUES('{fname}', '{lname}', '{gend}', '{pnumber}', '{email}', {age}, '{addr}', '{spec}', {yoe});"
    return executeQueryAndCommit(sql)

def getDoctorInfoById(docId):
    sql = f"SELECT * FROM doctors_management_system.doctors where doctor_id = {docId}; "
    docInfo = executeQueryAndReturnResult(sql)[1][0]
    print('stuinfo',docInfo)
    data = {'did': docInfo[0], 'fname': docInfo[1], 'lname': docInfo[2], 'gender': docInfo[3], 'pnumber': docInfo[4], 'email': docInfo[5], 'age': docInfo[6], 'address': docInfo[7], 'spec': docInfo[8], 'yoe': docInfo[9]}
    print(data)
    return data

def getDoctorIdsAndNames():
    sql =f"SELECT doctor_id, concat(first_name, ' ', last_name) as 'Doctor Name' FROM doctors_management_system.doctors;"
    return executeQueryAndReturnResult(sql)