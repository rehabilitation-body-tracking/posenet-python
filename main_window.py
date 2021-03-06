"""Shows main page, connect front and backend"""
import sys

from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtWidgets, uic

from count_exercises import count_exercises, ExercisesType

QT_FILE = "gui/med_rehab.ui"
UI_WINDOW, _ = uic.loadUiType(QT_FILE)


class MainWindow(QtWidgets.QMainWindow, UI_WINDOW):
    """Shows main window"""

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_WINDOW.__init__(self)

        self.setupUi(self)
        self.setWindowTitle("Medical Rehab App")

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(110, 400)

        btn = QtGui.QPushButton("Go to exercise", self)
        btn.clicked.connect(self.go_to_exercise)
        btn.resize(btn.minimumSizeHint())
        btn.move(400, 400)
        self.cb = QtGui.QComboBox(self)
        self.cb.addItems([
            "Squats", "Lifting right hand", "Lifting left hand", "Lifting left leg",
            "Lifting right leg", "Bends over", "Head's side bends", "Right elbow to left knee",
            "Left elbow to right knee"])
        self.cb.resize(self.cb.minimumSizeHint())
        self.cb.move(110, 250)

        self.show()

    def exercise_changed(self):
        pass

    def close_application(self):
        choice = QtGui.QMessageBox.question(
            self, 'Confirm exit', "Are you sure you want to exit?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def go_to_exercise(self):

        try:
            amount = int(WINDOW.amountEdit.text())
            if amount < 1:
                raise ValueError
        except ValueError:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Amount should be a digit and more than 0')
            error_dialog.exec_()
        else:
            if self.cb.currentText() == "Squats":
                count_exercises(amount, ExercisesType.SQUAT)
            elif self.cb.currentText() == "Lifting right hand":
                count_exercises(amount, ExercisesType.HANDS_RIGHT)
            elif self.cb.currentText() == "Lifting left hand":
                count_exercises(amount, ExercisesType.HANDS_LEFT)
            elif self.cb.currentText() == "Lifting right leg":
                count_exercises(amount, ExercisesType.LIFT_LEG_RIGHT)
            elif self.cb.currentText() == "Lifting left leg":
                count_exercises(amount, ExercisesType.LIFT_LEG_LEFT)
            elif self.cb.currentText() == "Bends over":
                count_exercises(amount, ExercisesType.BENDS)
            elif self.cb.currentText() == "Head's side bends":
                count_exercises(amount, ExercisesType.HEAD)
            elif self.cb.currentText() == "Right elbow to left knee":
                count_exercises(amount, ExercisesType.BEND_LEFT_KNEE)
            elif self.cb.currentText() == "Left elbow to right knee":
                count_exercises(amount, ExercisesType.BEND_RIGHT_KNEE)


if __name__ == '__main__':
    APP = QtWidgets.QApplication(sys.argv)
    WINDOW = MainWindow()
    WINDOW.show()
    APP.exec_()
