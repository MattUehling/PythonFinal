import csv

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from gui_login import Ui_login_page


class Logic_Login(QMainWindow, Ui_login_page):
    loginSuccessful = pyqtSignal()

    def __init__(self) -> None:
        """Creates the class"""
        super().__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.login)
        self.username = ''
        self.id = ''
        self.candidate = ''

    def login(self) -> None:
        """Saves the login information and calls the method to validate it """
        self.username = self.username_input.text().strip()
        self.id = self.id_input.text().strip()
        print("Login clicked")
        if self.validateInput():
            self.clearInput()
            self.loginSuccessful.emit()

    def validateInput(self) -> bool:
        """Validates the input based on the possible voters csv"""
        with open('Output.csv', 'r') as input_csv_file:
            print("Opened CSV")
            reader = csv.DictReader(input_csv_file)
            for row in reader:
                if row['Username'] == self.username and row['Id'] == self.id:
                    print("Valid candidate")
                    if row['Candidate']:  # Checking if the candidate field is not empty
                        print("Error")
                        self.clearInput()
                        self.error_message.setText("This user has already voted")
                        self.error_message.setStyleSheet("color: red")  # Change text color to red
                        return False
                elif row['Username'] == self.username and not row['Id'] == self.id:
                    print("Error")
                    self.clearInput()
                    self.error_message.setText("Enter a valid id")
                    self.error_message.setStyleSheet("color: red")
                    return False
                elif not row['Username'] == self.username and row['Id'] == self.id:
                    print("Error")
                    self.clearInput()
                    self.error_message.setText("Enter a valid username")
                    self.error_message.setStyleSheet("color: red")
                    return False
            return True

    def getUsername(self) -> str:
        """Returns the username"""
        return self.username

    def getId(self) -> str:
        """Returns the Id"""
        return self.id

    def clearInput(self) -> None :
        """Clears the input """
        self.error_message.setText("")
        self.username_input.clear()
        self.id_input.clear()
