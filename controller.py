from mysql_functions import *

def add_doctor(fname, lname, pnumber, email, age, gender, address, specilization,
                 yearsofexperience):
    sql = f"insert into doctors_management_system.doctors(first_name, last_name, gender, phone_number, email, age, address, specilization, years_of_experience) values('{fname}', '{lname}', '{gender}', '{pnumber}', '{email}', {age}, '{address}', '{specilization}', {yearsofexperience});"
    return executeQueryAndCommit(sql)