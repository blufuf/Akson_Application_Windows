import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import serial.tools.list_ports
from terminal import TerminalWindow
from terminal2 import TerminalWindow2  # Импорт нового терминала
from board1_window import Ui_Board1_window
from board2_window import Ui_Board2_window
from board3_window import Ui_board3_window
from board4_window import Ui_board4_window
import subprocess
import pyautogui
import time
import os
from datetime import datetime

import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"


def resource_path(relative_path):
    """Возвращает корректный путь к ресурсу (для exe и IDE)."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(188, 188, 188);")

        icon_path = resource_path("AksonICON.ico")
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_program = QtWidgets.QLabel(self.centralwidget)
        self.name_program.setGeometry(QtCore.QRect(0, 20, 801, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.name_program.setFont(font)
        self.name_program.setAlignment(QtCore.Qt.AlignCenter)
        self.name_program.setObjectName("name_program")
        self.text_select_port = QtWidgets.QLabel(self.centralwidget)
        self.text_select_port.setGeometry(QtCore.QRect(0, 90, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.text_select_port.setFont(font)
        self.text_select_port.setAlignment(QtCore.Qt.AlignCenter)
        self.text_select_port.setObjectName("text_select_port")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.port_box = QtWidgets.QComboBox(self.centralwidget)
        self.port_box.setGeometry(QtCore.QRect(240, 140, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.port_box.setFont(font)
        self.port_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.port_box.setAutoFillBackground(False)
        self.port_box.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.port_box.setObjectName("port_box")
        self.text_select_baudrate = QtWidgets.QLabel(self.centralwidget)
        self.text_select_baudrate.setGeometry(QtCore.QRect(0, 200, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.text_select_baudrate.setFont(font)
        self.text_select_baudrate.setAlignment(QtCore.Qt.AlignCenter)
        self.text_select_baudrate.setObjectName("text_select_baudrate")
        self.baudrate_box = QtWidgets.QComboBox(self.centralwidget)
        self.baudrate_box.setGeometry(QtCore.QRect(240, 270, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.baudrate_box.setFont(font)
        self.baudrate_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baudrate_box.setAutoFillBackground(False)
        self.baudrate_box.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.baudrate_box.setObjectName("baudrate_box")

        self.btn_open_cube = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_cube.setGeometry(QtCore.QRect(50, 200, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_open_cube.setFont(font)
        self.btn_open_cube.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_open_cube.setAutoFillBackground(False)
        self.btn_open_cube.setStyleSheet("\n"
                                             "background-color: rgb(221, 221, 221);")
        self.btn_open_cube.setObjectName("btn_open_cube")

        self.board_1_akson_xl_ex = QtWidgets.QPushButton(self.centralwidget)
        self.board_1_akson_xl_ex.setGeometry(QtCore.QRect(30, 360, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.board_1_akson_xl_ex.setFont(font)
        self.board_1_akson_xl_ex.setFocusPolicy(QtCore.Qt.NoFocus)
        self.board_1_akson_xl_ex.setStyleSheet("background-color: rgb(226, 226, 226);\n"
                                               "border-color: rgb(195, 195, 195);\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.board_1_akson_xl_ex.setShortcut("")
        self.board_1_akson_xl_ex.setObjectName("board_1_akson_xl_ex")

        self.board_2_akson_xl_ex = QtWidgets.QPushButton(self.centralwidget)
        self.board_2_akson_xl_ex.setGeometry(QtCore.QRect(220, 360, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.board_2_akson_xl_ex.setFont(font)
        self.board_2_akson_xl_ex.setStyleSheet("background-color: rgb(226, 226, 226);\n"
                                    "border-color: rgb(195, 195, 195);\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.board_2_akson_xl_ex.setObjectName("board_2_akson_xl_ex")

        # self.board_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.board_5.setGeometry(QtCore.QRect(30, 480, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.board_5.setFont(font)
        # self.board_5.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        #                            "border-color: rgb(195, 195, 195);\n"
        #                            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        # self.board_5.setObjectName("board_5")
        #
        # self.board_6 = QtWidgets.QPushButton(self.centralwidget)
        # self.board_6.setGeometry(QtCore.QRect(220, 480, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.board_6.setFont(font)
        # self.board_6.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        #                            "border-color: rgb(195, 195, 195);\n"
        #                            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        # self.board_6.setObjectName("board_6")

        self.board_3_akson_xl = QtWidgets.QPushButton(self.centralwidget)
        self.board_3_akson_xl.setGeometry(QtCore.QRect(430, 360, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.board_3_akson_xl.setFont(font)
        self.board_3_akson_xl.setStyleSheet("background-color: rgb(226, 226, 226);\n"
                                   "border-color: rgb(195, 195, 195);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.board_3_akson_xl.setObjectName("board_3_akson_xl")

        self.board_4_akson_1v1F = QtWidgets.QPushButton(self.centralwidget)
        self.board_4_akson_1v1F.setGeometry(QtCore.QRect(620, 360, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.board_4_akson_1v1F.setFont(font)
        self.board_4_akson_1v1F.setStyleSheet("background-color: rgb(226, 226, 226);\n"
                                   "border-color: rgb(195, 195, 195);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        self.board_4_akson_1v1F.setObjectName("board_4_akson_1v1F")

        self.btn_refresh_ports = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh_ports.setGeometry(QtCore.QRect(590, 140, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_refresh_ports.setFont(font)
        self.btn_refresh_ports.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_refresh_ports.setAutoFillBackground(False)
        self.btn_refresh_ports.setStyleSheet("\n"
                                             "background-color: rgb(221, 221, 221);")
        self.btn_refresh_ports.setObjectName("btn_refresh_ports")
        # self.board_7 = QtWidgets.QPushButton(self.centralwidget)
        # self.board_7.setGeometry(QtCore.QRect(430, 480, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.board_7.setFont(font)
        # self.board_7.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        #                            "border-color: rgb(195, 195, 195);\n"
        #                            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        # self.board_7.setObjectName("board_7")
        # self.board_8 = QtWidgets.QPushButton(self.centralwidget)
        # self.board_8.setGeometry(QtCore.QRect(620, 480, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.board_8.setFont(font)
        # self.board_8.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        #                            "border-color: rgb(195, 195, 195);\n"
        #                            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(132, 173, 169, 255), stop:1 rgba(255, 255, 255, 255));")
        # self.board_8.setObjectName("board_8")

        self.btn_open_putty = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_putty.setGeometry(QtCore.QRect(590, 200, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_open_putty.setFont(font)
        self.btn_open_putty.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_open_putty.setAutoFillBackground(False)
        self.btn_open_putty.setStyleSheet("\n"
                                          "background-color: rgb(221, 221, 221);")
        self.btn_open_putty.setObjectName("btn_open_putty")
        self.btn_open_putty.setText("Открыть PuTTy")

        # self.btn_exp = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_exp.setGeometry(QtCore.QRect(120, 470, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.btn_exp.setFont(font)
        # self.btn_exp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.btn_exp.setAutoFillBackground(False)
        # self.btn_exp.setStyleSheet("\n"
        #                                      "background-color: rgb(221, 221, 221);")
        # self.btn_exp.setObjectName("btn_exp")
        # self.btn_exp.setText("Экспортировать\nнастройки")
        #
        # self.btn_imp = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_imp.setGeometry(QtCore.QRect(530, 470, 150, 70))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.btn_imp.setFont(font)
        # self.btn_imp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.btn_imp.setAutoFillBackground(False)
        # self.btn_imp.setStyleSheet("\n"
        #                                      "background-color: rgb(221, 221, 221);")
        # self.btn_imp.setObjectName("btn_imp")
        # self.btn_imp.setText("Импортировать\nнастройки")
        #
        # self.line_exp = QtWidgets.QLineEdit(self.centralwidget)
        # self.line_exp.setGeometry(QtCore.QRect(50, 550, 280, 30))
        # font = QtGui.QFont()
        # font.setPointSizeF(12.0)
        # self.line_exp.setFont(font)
        # self.line_exp.setStyleSheet("background-color: rgb(221, 221, 221);")
        # self.line_exp.setText("")
        # self.line_exp.setObjectName("line_exp")
        # self.line_exp.setPlaceholderText("Название экспор-го файла")
        #
        # self.line_imp = QtWidgets.QLineEdit(self.centralwidget)
        # self.line_imp.setGeometry(QtCore.QRect(460, 550, 280, 30))
        # font = QtGui.QFont()
        # font.setPointSizeF(12.0)
        # self.line_imp.setFont(font)
        # self.line_imp.setStyleSheet("background-color: rgb(221, 221, 221);")
        # self.line_imp.setText("")
        # self.line_imp.setObjectName("line_imp")
        # self.line_imp.setPlaceholderText("Название импор-го файла")



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конфигуратор АКСОН"))
        self.name_program.setText(_translate("MainWindow", "Конфигуратор АКСОН"))
        self.text_select_port.setText(_translate("MainWindow", "Выберите порт"))
        self.text_select_baudrate.setText(_translate("MainWindow", "Выберите скорость порта"))
        self.board_1_akson_xl_ex.setText(_translate("MainWindow", "АКСОН XL EX\n"
                                                                  "(STM 32 L496)"))
        self.board_2_akson_xl_ex.setText(_translate("MainWindow", "АКСОН XL EX\n"
                                                       "(F101/F103)"))
        # self.board_5.setText(_translate("MainWindow", "АКСОН 1V1\n"
        #                                               "L496"))
        # self.board_6.setText(_translate("MainWindow", "АКСОН\n"
        #                                               "SHRP"))
        self.board_3_akson_xl.setText(_translate("MainWindow", "АКСОН XL\n"
                                                      "STM F101/F103"))
        self.board_4_akson_1v1F.setText(_translate("MainWindow", "АКСОН 1V1\n"
                                                      "F101/F103"))
        self.btn_refresh_ports.setText(_translate("MainWindow", "Обновить порты"))
        # self.board_7.setText(_translate("MainWindow", "АКСОН\n"
        #                                               "7"))
        # self.board_8.setText(_translate("MainWindow", "АКСОН\n"
        #                                               "8"))
        self.btn_open_cube.setText(_translate("MainWindow", "Открыть CUBE"))

        self.made_in_label = QtWidgets.QLabel(self.centralwidget)
        self.made_in_label.setGeometry(QtCore.QRect(630, 550, 160, 40))  # положение в правом нижнем углу
        self.made_in_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        pixmap = QtGui.QPixmap(resource_path("AksonIMG.png"))
        pixmap = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.flag_icon = QtWidgets.QLabel(self.centralwidget)
        self.flag_icon.setPixmap(pixmap)
        self.flag_icon.setGeometry(QtCore.QRect(605, 539, 64, 64))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.made_in_label.setFont(font)
        self.made_in_label.setText("Сделано в России")


class SerialApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.baudrate_box.addItems(
            [str(rate) for rate in [300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]])
        self.ui.baudrate_box.setCurrentText("115200")

        self.ui.btn_refresh_ports.clicked.connect(self.refresh_ports)
        self.ui.btn_open_cube.clicked.connect(self.open_stm32cubeprogrammer)
        self.ui.board_1_akson_xl_ex.clicked.connect(lambda: self.open_board1_interface())
        self.ui.board_2_akson_xl_ex.clicked.connect(lambda: self.open_board2_interface())
        self.ui.board_3_akson_xl.clicked.connect(lambda: self.open_board3_interface())
        self.ui.board_4_akson_1v1F.clicked.connect(lambda: self.open_board4_interface())
        # self.ui.board_5.clicked.connect(lambda: self.open_board_interface("Board5"))
        # self.ui.board_6.clicked.connect(lambda: self.open_board_interface("Board6"))
        # self.ui.board_7.clicked.connect(lambda: self.open_board_interface("Board7"))
        # self.ui.board_8.clicked.connect(lambda: self.open_board_interface("Board8"))
        self.ui.btn_open_putty.clicked.connect(self.open_putty)
        # self.ui.btn_exp.clicked.connect(self.show_export_warning)
        # self.ui.btn_imp.clicked.connect(self.show_import_warning)


        self.refresh_ports()

    def open_putty(self):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        putty_path = "C:\\Program Files\\PuTTY\\putty.exe"  # Путь к PuTTY

        if selected_port and selected_baudrate:
            try:
                subprocess.Popen([putty_path, "-serial", selected_port, "-sercfg", selected_baudrate])
            except FileNotFoundError:
                print("PuTTY не найден. Проверьте правильность пути.")

    def refresh_ports(self):
        ports = self.get_serial_ports()
        self.ui.port_box.clear()
        self.ui.port_box.addItems(ports)

    def get_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def open_board_interface(self, board_name):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        if selected_port and selected_baudrate:
            board_window = TerminalWindow2(board_name, selected_port, selected_baudrate, self)  # Используем TerminalWindow2
            board_window.exec_()

    def open_board1_interface(self):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        if selected_port and selected_baudrate:
            self.board1_window = QtWidgets.QMainWindow()
            self.board1_ui = Ui_Board1_window()
            self.board1_ui.setupUi(self.board1_window)

            self.terminal_widget = TerminalWindow("АКСОН XL EX (STM 32 L496)", selected_port, selected_baudrate, self.board1_window)
            terminal_layout = QtWidgets.QVBoxLayout(self.board1_ui.terminal_window)
            terminal_layout.addWidget(self.terminal_widget)
            self.board1_ui.terminal_widget = self.terminal_widget
            self.board1_window.show()

    def open_board2_interface(self):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        if selected_port and selected_baudrate:
            self.board2_window = QtWidgets.QMainWindow()
            self.board2_ui = Ui_Board2_window()
            self.board2_ui.setupUi(self.board2_window)

            self.terminal_widget = TerminalWindow("АКСОН XL EX (F101/F103)", selected_port, selected_baudrate, self.board2_window)
            terminal_layout = QtWidgets.QVBoxLayout(self.board2_ui.terminal_window)
            terminal_layout.addWidget(self.terminal_widget)
            self.board2_ui.terminal_widget = self.terminal_widget
            self.board2_window.show()

    def open_board3_interface(self):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        if selected_port and selected_baudrate:
            self.board3_window = QtWidgets.QMainWindow()
            self.board3_ui = Ui_board3_window()
            self.board3_ui.setupUi(self.board3_window)

            self.terminal_widget = TerminalWindow("АКСОН XL STM F101/F103", selected_port, selected_baudrate, self.board3_window)
            terminal_layout = QtWidgets.QVBoxLayout(self.board3_ui.terminal_window)
            terminal_layout.addWidget(self.terminal_widget)
            self.board3_ui.terminal_widget = self.terminal_widget
            self.board3_window.show()

    def open_board4_interface(self):
        selected_port = self.ui.port_box.currentText()
        selected_baudrate = self.ui.baudrate_box.currentText()
        if selected_port and selected_baudrate:
            self.board4_window = QtWidgets.QMainWindow()
            self.board4_ui = Ui_board4_window()
            self.board4_ui.setupUi(self.board4_window)

            self.terminal_widget = TerminalWindow2("АКСОН 1V1 F101/F103", selected_port, selected_baudrate, self.board4_window)  # Используем TerminalWindow2
            terminal_layout = QtWidgets.QVBoxLayout(self.board4_ui.terminal_window)
            terminal_layout.addWidget(self.terminal_widget)
            self.board4_ui.terminal_widget = self.terminal_widget
            self.board4_window.show()

    def open_stm32cubeprogrammer(self):
        # Попробуем найти STM32CubeProgrammer в системе
        possible_paths = [
            r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe",
            r"C:\Program Files (x86)\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe"
        ]

        stm32cubeprogrammer_path = None

        for path in possible_paths:
            if os.path.exists(path):
                stm32cubeprogrammer_path = path
                break

        # Если не найдено — попробуем открыть через PATH
        if stm32cubeprogrammer_path is None:
            for path in os.environ["PATH"].split(";"):
                exe_path = os.path.join(path, "STM32CubeProgrammer.exe")
                if os.path.exists(exe_path):
                    stm32cubeprogrammer_path = exe_path
                    break

        # Если всё ещё None — покажем ошибку
        if stm32cubeprogrammer_path is None:
            print("⚠️ STM32CubeProgrammer не найден. Проверьте установку.")
            return

        stm32cubeprogrammer_dir = os.path.dirname(stm32cubeprogrammer_path)

        try:
            self.close_port_connection()
            subprocess.Popen([stm32cubeprogrammer_path], cwd=stm32cubeprogrammer_dir)
        except Exception as e:
            print(f"Ошибка при запуске STM32CubeProgrammer: {e}")

    def close_port_connection(self):
        if hasattr(self, 'serial_thread') and self.serial_thread.isRunning():
            self.serial_thread.terminate()
            self.serial_thread.wait()
            print("Соединение с портом закрыто")

#     def show_export_warning(self):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Warning)
#         msg.setWindowTitle("Подтверждение экспорта")
#         msg.setText("ВАЖНО!!!\n\n"
#                     "1. Откройте HyperTerminal\n\n"
#                     "2. Подключитесь к нужному Вам порту и выберите скорость порта\n\n"
#                     "3. Переключите язык на ENG\n\n"
#                     "Не трогайте клавиатуру и мышь пока выполняется экспорт\n\n"
#                     "Если все пункты выполнены, нажмите Выполнить")
#         msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#         msg.button(QMessageBox.Yes).setText("Выполнить")
#         msg.button(QMessageBox.No).setText("Отмена")
#
#         retval = msg.exec_()
#
#         if retval == QMessageBox.Yes:
#             self.export_settings()
#
#     def show_import_warning(self):
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Warning)
#         msg.setWindowTitle("Подтверждение импорта")
#         msg.setText("1. Откройте HyperTerminal\n\n"
#                     "2. Подключитесь к нужному Вам порту и выберите скорость порта\n\n"
#                     "3. Переключите язык на ENG\n\n"
#                     "Не трогайте клавиатуру и мышь пока выполняется экспорт\n\n"
#                     "Если все пункты выполнены, нажмите Выполнить")
#         msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#         msg.button(QMessageBox.Yes).setText("Выполнить")
#         msg.button(QMessageBox.No).setText("Отмена")
#
#         retval = msg.exec_()
#
#         if retval == QMessageBox.Yes:
#             self.import_settings()
#
#     def export_settings(self):
#         file_name_prefix = self.ui.line_exp.text()
#         if not file_name_prefix:
#             print("Введите название файла.")
#             return
#
#         current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         file_name = f"{file_name_prefix}_{current_date}"
#
#         self.automate_export(file_name)
#
#     def automate_export(self, file_name):
#         activate_terminal_window()
#         enter_export_command()
#         navigate_receive_file()
#         save_file(file_name)
#
#     def import_settings(self):
#         file_name_prefix = self.ui.line_imp.text()
#         if not file_name_prefix:
#             print("Введите название файла.")
#             return
#
#         file_name2 = file_name_prefix
#
#         self.automate_import(file_name2)
#
#     def automate_import(self, file_name2):
#         activate_terminal_window2()
#         enter_import_command()
#         navigate_receive_file2(file_name2)
#
#
# def activate_terminal_window():
#     windows = pyautogui.getWindowsWithTitle('HyperTerminal')
#     if windows:
#         window = windows[0]
#         window.maximize()
#         window.activate()
#         time.sleep(1)  # Даем время окну на активацию
#     else:
#         print("HyperTerminal не найден. Убедитесь, что программа запущена.")
#
# def enter_export_command():
#     time.sleep(1)
#     pyautogui.typewrite('\nxsets exp\n', interval=0.1)
#     time.sleep(1)  # Ожидание выполнения команды
#
# def navigate_receive_file():
#     pyautogui.hotkey('alt', 't')
#     time.sleep(0.5)
#
#     pyautogui.press('r')
#     time.sleep(1)
#
#     pyautogui.hotkey('ctrl', 'a')
#     pyautogui.press('backspace')
#     pyautogui.typewrite('C:\\test')
#     pyautogui.press('tab')
#     pyautogui.press('tab')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('tab')
#     pyautogui.press('enter')
#     time.sleep(1)
#
# def save_file(file_name):
#     pyautogui.typewrite(file_name, interval=0.1)
#     time.sleep(0.5)
#
#     pyautogui.press('enter')
#     time.sleep(5)  # Ожидание завершения операции сохранения
#
# def activate_terminal_window2():
#     windows = pyautogui.getWindowsWithTitle('HyperTerminal')
#     if windows:
#         window = windows[0]
#         window.maximize()
#         window.activate()
#         time.sleep(1)  # Даем время окну на активацию
#     else:
#         print("HyperTerminal не найден. Убедитесь, что программа запущена.")
#
# def enter_import_command():
#     # Даем время для того, чтобы окно стало активным и готовым к вводу
#     time.sleep(1)
#     pyautogui.typewrite('\n xsets imp\n', interval=0.1)
#     time.sleep(1)  # Ожидание выполнения команды
#
# def navigate_receive_file2(file_name2):
#     pyautogui.hotkey('alt', 't')
#     time.sleep(0.5)
#
#     pyautogui.press('enter')
#     time.sleep(1)
#
#
#     pyautogui.typewrite(f'C:\\test\\{file_name2}')
#     pyautogui.press('tab')
#     pyautogui.press('tab')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('up')
#     pyautogui.press('tab')
#     pyautogui.press('enter')
#     time.sleep(1)
#
#
#     pyautogui.press('enter')
#     time.sleep(5)  # Ожидание завершения операции сохранения
#




if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = SerialApp()
        main_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(f"An error occurred: {str(e)}\n")
        print(f"An error occurred: {str(e)}")
