import math
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import *
from gui import *
import time


class logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_equals.clicked.connect(lambda: self.equals())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_on.clicked.connect(lambda: self.on())
        self.button_off.clicked.connect(lambda: self.off())
        self.button_delete.clicked.connect(lambda: self.delete())
        self.button_plus.clicked.connect(lambda: self.add())
        self.button_minus.clicked.connect(lambda: self.subtract())
        self.button_multiply.clicked.connect(lambda: self.multiply())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_open_bracket.clicked.connect(lambda: self.openBracket())
        self.button_close_bracket.clicked.connect(lambda: self.closeBracket())
        self.button_e.clicked.connect(lambda: self.e())
        self.button_pi.clicked.connect(lambda: self.pi())
        self.button_sqrt.clicked.connect(lambda: self.sqrt())
        self.button_power2.clicked.connect(lambda: self.power())
        self.button1.clicked.connect(lambda: self.one())
        self.button2.clicked.connect(lambda: self.two())
        self.button3.clicked.connect(lambda: self.three())
        self.button4.clicked.connect(lambda: self.four())
        self.button5.clicked.connect(lambda: self.five())
        self.button6.clicked.connect(lambda: self.six())
        self.button7.clicked.connect(lambda: self.seven())
        self.button8.clicked.connect(lambda: self.eight())
        self.button9.clicked.connect(lambda: self.nine())

        self.stack = []
        self.result = 0

    def fillLine(self):
        stack_text = ' '.join(map(str, self.stack))  # Join stack elements into a single string
        self.display.setText(stack_text)

    def delete(self):
        self.stack.pop()
        self.fillLine()

    def off(self):
        self.clear()
        self.display.setText('Powering off')
        QTimer.singleShot(3000, QApplication.quit)  # Quit the application after 3 seconds

    def on(self):
        self.display.setText('Ti-Matt is on')

    def add(self):
        self.stack.append('+')
        self.fillLine()

    def subtract(self):
        self.stack.append('-')
        self.fillLine()

    def multiply(self):
        self.stack.append('*')
        self.fillLine()

    def divide(self):
        self.stack.append('/')
        self.fillLine()

    def pi(self):
        self.stack.append(math.pi)
        self.fillLine()

    def e(self):
        self.stack.append(math.e)
        self.fillLine()

    def openBracket(self):
        self.stack.append('(')
        self.fillLine()

    def closeBracket(self):
        self.stack.append(')')
        self.fillLine()

    def sqrt(self):
        self.stack.append('√')
        self.openBracket()
        self.fillLine()

    def power(self):
        self.stack.append('power')
        self.fillLine()

    def one(self):
        self.stack.append(1)
        self.fillLine()

    def two(self):
        self.stack.append(2)
        self.fillLine()

    def three(self):
        self.stack.append(3)
        self.fillLine()

    def four(self):
        self.stack.append(4)
        self.fillLine()

    def five(self):
        self.stack.append(5)
        self.fillLine()

    def six(self):
        self.stack.append(6)
        self.fillLine()

    def seven(self):
        self.stack.append(7)
        self.fillLine()

    def eight(self):
        self.stack.append(8)
        self.fillLine()

    def nine(self):
        self.stack.append(9)
        self.fillLine()

    def equals(self):
        operators = {'+', '-', '*', '/', '√'}
        print("equals")
        while len(self.stack) != 1:
            if self.stack.__sizeof__() > 2:
                number1 = self.stack.pop()
                print(f'{number1} pop one')
                token2 = self.stack.pop()
                print(f'{token2} pop two')
                number2 = self.stack.pop()
                print(f'{number2} pop three')
                if number1.isDigit() and number2.isDigit() and not token2.isDigit():
                    if token2 == '+':
                        self.result = number1 + number2
                    elif token2 == '-':
                        self.result = number1 - number2
                    elif token2 == '*':
                        self.result = number1 * number2
                    elif token2 == '/':
                        if number2 == 0:
                            self.display.setText("Division by zero")
                            return
                        self.result = number1 / number2
                    elif token2 == '√':
                        self.result = math.sqrt(number1)
                    self.stack.append(self.result)
            if len(self.stack) == 1:
                print(self.stack[0])
                self.display.setText(str(self.stack[0]))
            else:
                self.display.setText("Invalid expression")

    def clear(self):
        self.display.setText('')
        self.stack.clear()
