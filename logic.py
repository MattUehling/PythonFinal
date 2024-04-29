from PyQt6.QtWidgets import QMainWindow
from gui import Ui_MainWindow


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())
        self.result_button.clicked.connect(lambda: self.results())
        self.candidate1_vote_total: int = 0
        self.candidate2_vote_total: int = 0

    def submit(self) -> None:
        if self.candidate1_button.isChecked():
            self.candidate1_vote_total += 1
            self.candidate1_button.setChecked(False)
        elif self.candidate2_button.isChecked():
            self.candidate2_vote_total += 1
            self.candidate2_button.setChecked(False)
        else:
            self.result_text.setText("Please select one candidate.")
        if self.candidate1_button.isChecked() or self.candidate2_button.isChecked():
            self.result_text.setText("")

    def clear(self) -> None:
        self.candidate1_button.setChecked(False)
        self.candidate2_button.setChecked(False)

        self.result_text.setText("Please select one of the candidates to vote for.")
        self.candidate1_vote_total = 0
        self.candidate2_vote_total = 0

    def results(self) -> None:
        self.result_text.setText(
            f'The current votes are:\n John: {self.candidate1_vote_total}\n Jane: {self.candidate2_vote_total}')
