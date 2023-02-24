drop database if exists doctors_management_system;
create database doctors_management_system;

use doctors_management_system;

create table doctors(
	doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    phone_number VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    address VARCHAR(50) NOT NULL,
	specilization VARCHAR(50) NOT NULL,
	years_of_experience INT NOT NULL
);

create table patients(
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    phone_number VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    address VARCHAR(50) NOT NULL
);