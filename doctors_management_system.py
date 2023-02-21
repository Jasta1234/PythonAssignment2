import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *


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
        uic.loadUi('home.ui', self)
