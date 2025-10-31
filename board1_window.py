import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import subprocess

def resource_path(relative_path):
    """Возвращает корректный путь к файлу (работает и в exe, и в IDE)."""
    try:
        base_path = sys._MEIPASS  # временная папка PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Ui_Board1_window(object):
    def setupUi(self, Board1_window):



        Board1_window.setObjectName("Board1_window")
        Board1_window.setFixedSize(1600, 910)
        Board1_window.setStyleSheet("background-color: rgb(168, 168, 168);")

        icon_path = resource_path("AksonICON.ico")
        Board1_window.setWindowIcon(QtGui.QIcon(icon_path))

        self.centralwidget = QtWidgets.QWidget(Board1_window)
        self.centralwidget.setObjectName("centralwidget")

        self.terminal_window = QtWidgets.QWidget(self.centralwidget)
        self.terminal_window.setGeometry(QtCore.QRect(870, 0, 730, 900))
        self.terminal_window.setObjectName("terminal_window")

        self.data_window = QtWidgets.QFrame(self.centralwidget)
        self.data_window.setGeometry(QtCore.QRect(20, 20, 710, 201))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.data_window.setStyleSheet("")
        self.data_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_window.setObjectName("data_window")

        self.text_guid = QtWidgets.QPushButton(self.data_window)
        self.text_guid.setGeometry(QtCore.QRect(0, 0, 190, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.text_guid.setFont(font)
        self.text_guid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.text_guid.setObjectName("text_guid")


        self.line_guid = QtWidgets.QLineEdit(self.data_window)
        self.line_guid.setGeometry(QtCore.QRect(190, 0, 520, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.line_guid.setFont(font)
        self.line_guid.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.line_guid.setText("")
        self.line_guid.setObjectName("line_guid")
        self.line_guid.setPlaceholderText("GUID")

        self.line_box_sets = QtWidgets.QLineEdit(self.data_window)
        self.line_box_sets.setGeometry(QtCore.QRect(190, 40, 520, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.line_box_sets.setFont(font)
        self.line_box_sets.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                         "color: rgb(255, 255, 255);")
        self.line_box_sets.setText("")
        self.line_box_sets.setObjectName("line_box_sets")
        self.line_box_sets.setPlaceholderText("Box Sets Key")

        self.btn_window = QtWidgets.QFrame(self.centralwidget)
        self.btn_window.setGeometry(QtCore.QRect(20, 250, 841, 571))
        self.btn_window.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.btn_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_window.setObjectName("btn_window")

        self.btn_entermoduls = QtWidgets.QToolButton(self.btn_window)
        self.btn_entermoduls.setGeometry(QtCore.QRect(102, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_entermoduls.setFont(font)
        self.btn_entermoduls.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_entermoduls.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_entermoduls.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_entermoduls.setAutoRaise(False)
        self.btn_entermoduls.setArrowType(QtCore.Qt.NoArrow)
        self.btn_entermoduls.setObjectName("btn_entermoduls")

        self.btn_entermoduls_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_entermoduls_check.setGeometry(QtCore.QRect(20, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_entermoduls_check.setFont(font)
        self.btn_entermoduls_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_entermoduls_check.setObjectName("btn_entermoduls_check")

        self.btn_gprs_sett = QtWidgets.QToolButton(self.btn_window)
        self.btn_gprs_sett.setGeometry(QtCore.QRect(342, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_gprs_sett.setFont(font)
        self.btn_gprs_sett.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_gprs_sett.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_gprs_sett.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_gprs_sett.setAutoRaise(False)
        self.btn_gprs_sett.setArrowType(QtCore.Qt.NoArrow)
        self.btn_gprs_sett.setObjectName("btn_gprs_sett")

        self.btn_gprs_sett_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_gprs_sett_check.setGeometry(QtCore.QRect(260, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_gprs_sett_check.setFont(font)
        self.btn_gprs_sett_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_gprs_sett_check.setObjectName("btn_gprs_sett_check")

        self.alkc_line = QtWidgets.QLineEdit(self.btn_window)
        self.alkc_line.setGeometry(QtCore.QRect(184, 340, 246, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.alkc_line.setFont(font)
        self.alkc_line.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.alkc_line.setText("ALKC")
        self.alkc_line.setObjectName("alkc_line")

        self.model_line = QtWidgets.QLineEdit(self.btn_window)
        self.model_line.setGeometry(QtCore.QRect(184, 380, 246, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.model_line.setFont(font)
        self.model_line.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.model_line.setText("022")
        self.model_line.setObjectName("model_line")

        self.date_line = QtWidgets.QLineEdit(self.btn_window)
        self.date_line.setGeometry(QtCore.QRect(184, 420, 246, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.date_line.setFont(font)
        self.date_line.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.date_line.setInputMask("00.00.0000;_")
        self.date_line.setPlaceholderText("дд.мм.гггг")

        self.date_line.setText("")
        self.date_line.setObjectName("date_line")

        self.limit_line = QtWidgets.QLineEdit(self.btn_window)
        self.limit_line.setGeometry(QtCore.QRect(184, 460, 246, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.limit_line.setFont(font)
        self.limit_line.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 255, 255);")
        self.limit_line.setText("0")
        self.limit_line.setObjectName("limit_line")


        self.btn_box_sets = QtWidgets.QPushButton(self.btn_window)
        self.btn_box_sets.setGeometry(QtCore.QRect(102, 340, 82, 160))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_box_sets.setFont(font)
        self.btn_box_sets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_box_sets.setObjectName("btn_box_sets")

        self.btn_check_box_sets = QtWidgets.QPushButton(self.btn_window)
        self.btn_check_box_sets.setGeometry(QtCore.QRect(20, 340, 82, 160))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_check_box_sets.setFont(font)
        self.btn_check_box_sets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_check_box_sets.setObjectName("btn_check_box_sets")

        self.btn_box_sets_clear = QtWidgets.QPushButton(self.btn_window)
        self.btn_box_sets_clear.setGeometry(QtCore.QRect(20, 500, 164, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_box_sets_clear.setFont(font)
        self.btn_box_sets_clear.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_box_sets_clear.setObjectName("btn_box_sets_clear")

        self.btn_corrtype = QtWidgets.QToolButton(self.btn_window)
        self.btn_corrtype.setGeometry(QtCore.QRect(342, 140, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_corrtype.setFont(font)
        self.btn_corrtype.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_corrtype.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_corrtype.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_corrtype.setAutoRaise(False)
        self.btn_corrtype.setArrowType(QtCore.Qt.NoArrow)
        self.btn_corrtype.setObjectName("btn_corrtype")

        self.btn_corrsett = QtWidgets.QToolButton(self.btn_window)
        self.btn_corrsett.setGeometry(QtCore.QRect(342, 210, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_corrsett.setFont(font)
        self.btn_corrsett.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_corrsett.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_corrsett.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_corrsett.setAutoRaise(False)
        self.btn_corrsett.setArrowType(QtCore.Qt.NoArrow)
        self.btn_corrsett.setObjectName("btn_corrsett")

        self.btn_corrtype_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_corrtype_check.setGeometry(QtCore.QRect(260, 140, 82, 140))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_corrtype_check.setFont(font)
        self.btn_corrtype_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_corrtype_check.setObjectName("btn_corrtype_check")

        self.btn_dev = QtWidgets.QToolButton(self.btn_window)
        self.btn_dev.setGeometry(QtCore.QRect(20, 140, 165, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_dev.setFont(font)
        self.btn_dev.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_dev.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_dev.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_dev.setAutoRaise(False)
        self.btn_dev.setArrowType(QtCore.Qt.NoArrow)
        self.btn_dev.setObjectName("btn_dev")

        self.btn_portsets = QtWidgets.QToolButton(self.btn_window)
        self.btn_portsets.setGeometry(QtCore.QRect(102, 240, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_portsets.setFont(font)
        self.btn_portsets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_portsets.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_portsets.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_portsets.setAutoRaise(False)
        self.btn_portsets.setArrowType(QtCore.Qt.NoArrow)
        self.btn_portsets.setObjectName("btn_portsets")

        self.btn_portsets_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_portsets_check.setGeometry(QtCore.QRect(20, 240, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_portsets_check.setFont(font)
        self.btn_portsets_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_portsets_check.setObjectName("btn_portsets_check")

        self.btn_datatime = QtWidgets.QPushButton(self.btn_window)
        self.btn_datatime.setGeometry(QtCore.QRect(660, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_datatime.setFont(font)
        self.btn_datatime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_datatime.setObjectName("btn_datatime")

        self.btn_settime =QtWidgets.QPushButton(self.btn_window)
        self.btn_settime.setGeometry(QtCore.QRect(742, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_settime.setFont(font)
        self.btn_settime.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_settime.setObjectName("btn_settime")

        self.btn_timesets_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_timesets_check.setGeometry(QtCore.QRect(660, 140, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_timesets_check.setFont(font)
        self.btn_timesets_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_timesets_check.setObjectName("btn_timesets_check")

        self.btn_timesets =QtWidgets.QPushButton(self.btn_window)
        self.btn_timesets.setGeometry(QtCore.QRect(742, 140, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_timesets.setFont(font)
        self.btn_timesets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_timesets.setObjectName("btn_timesets")

        self.btn_update_guid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update_guid.setGeometry(QtCore.QRect(740, 20, 137, 81))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_update_guid.setFont(font)
        self.btn_update_guid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_update_guid.setObjectName("btn_update_guid")

        self.btn_upload = QtWidgets.QPushButton(self.data_window)
        self.btn_upload.setGeometry(QtCore.QRect(0, 40, 190, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_upload.setFont(font)
        self.btn_upload.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_upload.setObjectName("btn_upload")

        # Кнопки бедствия
        self.btn_erase_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_erase_data.setGeometry(QtCore.QRect(20, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_erase_data.setFont(font)
        self.btn_erase_data.setStyleSheet("background-color: rgb(255, 71, 71);")
        self.btn_erase_data.setObjectName("btn_erase_data")

        self.btn_erase_flash = QtWidgets.QPushButton(self.centralwidget)
        self.btn_erase_flash.setGeometry(QtCore.QRect(140, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_erase_flash.setFont(font)
        self.btn_erase_flash.setStyleSheet("background-color: rgb(255, 71, 71);")
        self.btn_erase_flash.setObjectName("btn_erase_flash")

        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(760, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_reset.setObjectName("btn_reset")

        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(640, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_help.setFont(font)
        self.btn_help.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_help.setObjectName("btn_help")

        self.btn_ver = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver.setGeometry(QtCore.QRect(520, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_ver.setFont(font)
        self.btn_ver.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_ver.setObjectName("btn_ver")

        self.btn_exit_cross = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit_cross.setGeometry(QtCore.QRect(400, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_exit_cross.setFont(font)
        self.btn_exit_cross.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_exit_cross.setObjectName("btn_exit_cross")




        Board1_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Board1_window)
        self.statusbar.setObjectName("statusbar")
        Board1_window.setStatusBar(self.statusbar)
        self.retranslateUi(Board1_window)
        QtCore.QMetaObject.connectSlotsByName(Board1_window)




        # Подключаем слоты к кнопкам
        self.btn_datatime.clicked.connect(self.send_datetime_command)
        self.btn_entermoduls.clicked.connect(self.show_module_menu)
        self.btn_gprs_sett.clicked.connect(self.show_gprs_menu)
        self.btn_corrtype.clicked.connect(self.show_corrtype_menu)
        self.btn_corrsett.clicked.connect(self.show_corrsett_menu)
        self.btn_entermoduls_check.clicked.connect(self.send_modules_sets_command)
        self.btn_gprs_sett_check.clicked.connect(self.send_btn_gprs_sett_check)
        self.btn_corrtype_check.clicked.connect(self.send_btn_corrtype_check)
        self.btn_settime.clicked.connect(self.send_settime)
        self.btn_update_guid.clicked.connect(self.update_guid_command)
        self.btn_upload.clicked.connect(self.update_box_key)
        self.btn_erase_data.clicked.connect(self.send_erase_data)
        self.btn_erase_flash.clicked.connect(self.send_erase_flash)
        self.btn_reset.clicked.connect(self.send_reset)
        self.btn_help.clicked.connect(self.send_help)
        self.btn_check_box_sets.clicked.connect(self.send_btn_check_boxsets)
        self.btn_box_sets.clicked.connect(self.send_btn_boxsets)
        self.btn_portsets_check.clicked.connect(self.send_portsets_check)
        self.btn_portsets.clicked.connect(self.show_portsett_menu)
        self.btn_dev.clicked.connect(self.send_dev)
        self.btn_ver.clicked.connect(self.send_ver)
        self.btn_box_sets_clear.clicked.connect(self.send_box_sets_clear)
        self.text_guid.clicked.connect(self.send_general_sets)
        self.btn_exit_cross.clicked.connect(self.send_exit_cross)
        self.btn_timesets.clicked.connect(self.show_timesets)
        self.btn_timesets_check.clicked.connect(self.send_timesets_check)


        Board1_window.closeEvent = self.closeEvent


    def retranslateUi(self, Board1_window):
        _translate = QtCore.QCoreApplication.translate
        Board1_window.setWindowTitle(_translate("Board1_window", "АКСОН XL EX (STM 32 L496)"))

        self.btn_entermoduls.setText(_translate("Board1_window", "Выбор\nмодуля"))
        self.btn_gprs_sett.setText(_translate("Board1_window", "Настрой-\nки\nGPRS"))
        self.btn_box_sets.setText(_translate("Board1_window", "Box\nget"))
        self.btn_check_box_sets.setText(_translate("Board1_window", "Проверка\nBox\nsets"))
        self.btn_corrtype.setText(_translate("Board1_window", "Тип\nкорректора"))
        self.btn_dev.setText(_translate("Board1_window", "Dev"))
        self.btn_portsets.setText(_translate("Board1_window", "Port\nsets"))
        self.btn_datatime.setText(_translate("Board1_window", "Проверка\ndatatime"))
        self.btn_update_guid.setText(_translate("Board1_window", "Установить\n"
        "GUID"))
        self.btn_upload.setText(_translate("Board1_window", "Установить key"))
        self.btn_entermoduls_check.setText(_translate("Board1_window", "Про-\nверка"))
        self.btn_gprs_sett_check.setText(_translate("Board1_window", "Про-\nверка"))
        self.btn_corrtype_check.setText(_translate("Board1_window", "Про-\nверка"))
        self.btn_portsets_check.setText(_translate("Board1_window", "Про-\nверка"))
        self.btn_settime.setText(_translate("Board1_window", "Устано-\nвить\ndatetime"))
        self.btn_erase_data.setText(_translate("Board1_window", "Erase Data"))
        self.btn_erase_flash.setText(_translate("Board1_window", "Erase Flash"))
        self.btn_reset.setText(_translate("Board1_window", "Reset"))
        self.btn_help.setText(_translate("Board1_window", "Help"))
        self.btn_corrsett.setText(_translate("Board1_window", "Настройки\nкорректора"))
        self.btn_ver.setText(_translate("Board1_window", "Ver"))
        self.btn_box_sets_clear.setText(_translate("Board1_window", "Очистить box sets"))
        self.text_guid.setText(_translate("Board1_window", "general_sets"))
        self.btn_exit_cross.setText(_translate("Board1_window", "Exit Cross"))
        self.btn_timesets_check.setText(_translate("Board1_window", "Проверка"))
        self.btn_timesets.setText(_translate("Board1_window", "Time\nsets"))


    def show_timesets(self):
        menu = QtWidgets.QMenu(self.btn_timesets)

        src_server = QtWidgets.QAction("Server",self.btn_timesets)
        src_ntp = QtWidgets.QAction("NTP",self.btn_timesets)

        src_server.triggered.connect(lambda: self.send_module_command("time_sets src server"))
        src_ntp.triggered.connect(lambda: self.send_module_command("time_sets src ntp"))

        menu.addAction(src_server)
        menu.addAction(src_ntp)

        menu.exec_(QtGui.QCursor.pos())

    def send_timesets_check(self):
        self.terminal_widget.send_data('time_sets')

    def send_exit_cross(self):
        self.terminal_widget.send_data('+++++')

    def send_general_sets(self):
        self.terminal_widget.send_data('general_sets')

    def closeEvent(self, event):
        try:
            self.terminal_widget.stop_serial_thread()  # Закрываем соединение, если это необходимо
            event.accept()
        except Exception as e:
            print(f"Error in closeEvent: {str(e)}")
            event.ignore()


    def send_box_sets_clear(self):
        self.terminal_widget.send_data('box_sets clear')

    def send_ver(self):
        self.terminal_widget.send_data('ver')

    def send_dev(self):
        self.terminal_widget.send_data('dev corrector -see -time')

    def send_portsets_check(self):
        self.terminal_widget.send_data('port_sets')

    def send_erase_flash(self):
        self.terminal_widget.send_data('erase flash')

    def send_erase_data(self):
        self.terminal_widget.send_data('erase data')

    def send_reset(self):
        self.terminal_widget.send_data('reset')

    def send_help(self):
        self.terminal_widget.send_data('help')

    def send_settime(self):
        current_date = datetime.datetime.now()
        current_date_string = current_date.strftime('%d.%m.%Y %H:%M:%S')
        self.terminal_widget.send_data(f'datetime {current_date_string}')

    def send_modules_sets_command(self):
        self.terminal_widget.send_data('modules_sets')

    def send_btn_gprs_sett_check(self):
        self.terminal_widget.send_data('gprs_sets')

    def send_btn_corrtype_check(self):
        self.terminal_widget.send_data('corrector')

    def send_datetime_command(self):
        self.terminal_widget.send_data('datetime')

    def update_guid_command(self):
        guid_value = self.line_guid.text()
        self.terminal_widget.send_data(f'general_sets guid {guid_value}')


    def update_box_key(self):
        box_key = self.line_box_sets.text()
        self.terminal_widget.send_data('box_sets key')
        self.terminal_widget.send_data(f'{box_key}')

    def send_btn_check_boxsets(self):
        self.terminal_widget.send_data('box_sets')

    def send_btn_boxsets(self):
        alkc_value = self.alkc_line.text()
        model_value = self.model_line.text()
        date_value = self.date_line.text()
        limit_value = self.limit_line.text()
        self.terminal_widget.send_data(f'box_sets num {alkc_value}')
        self.terminal_widget.send_data(f'box_sets model {model_value}')
        self.terminal_widget.send_data(f'box_sets date {date_value}')
        self.terminal_widget.send_data(f'box_sets limit {limit_value}')
        self.terminal_widget.send_data('box_sets get')

    def show_module_menu(self):
        # Создание выпадающего меню для кнопки Enter Modules
        menu = QtWidgets.QMenu(self.btn_entermoduls)

        # Создание подменю для Module 1 и Module 2
        module1_menu = QtWidgets.QMenu("Module 1", self.btn_entermoduls)
        module2_menu = QtWidgets.QMenu("Module 2", self.btn_entermoduls)

        # Создание подменю для ON и OFF в каждом Module
        on_menu1 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action1 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action1.triggered.connect(lambda: self.send_module_command("modules_sets 1 off\r\n"
                                                                        "modules_sets"))

        on_menu2 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action2 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action2.triggered.connect(lambda: self.send_module_command("modules_sets 2 off\r\n"
                                                                        "modules_sets"))

        # Добавление команд GPRS, CSD и ALL в подменю ON
        gprs_action1 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action1 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action1 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action1.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 gprs\r\n"
                                                                        "modules_sets"))
        csd_action1.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 csd\r\n"
                                                                        "modules_sets"))
        all_action1.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 all\r\n"
                                                                        "modules_sets"))

        on_menu1.addAction(gprs_action1)
        on_menu1.addAction(csd_action1)
        on_menu1.addAction(all_action1)

        gprs_action2 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action2 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action2 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action2.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 gprs\r\n"
                                                                        "modules_sets"))

        csd_action2.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 csd\r\n"
                                                                        "modules_sets"))
        all_action2.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 all\r\n"
                                                                        "modules_sets"))

        on_menu2.addAction(gprs_action2)
        on_menu2.addAction(csd_action2)
        on_menu2.addAction(all_action2)

        # Добавление подменю ON и OFF в Module 1 и Module 2
        module1_menu.addMenu(on_menu1)
        module1_menu.addAction(off_action1)

        module2_menu.addMenu(on_menu2)
        module2_menu.addAction(off_action2)

        # Добавление Module 1 и Module 2 в основное меню
        menu.addMenu(module1_menu)
        menu.addMenu(module2_menu)

        # Отображение меню
        menu.exec_(QtGui.QCursor.pos())

    def show_gprs_menu(self):
        # Создание выпадающего меню для кнопки GPRS settings
        menu = QtWidgets.QMenu(self.btn_gprs_sett)

        # Создание подменю для Module 1 и Module 2
        module1_menu = QtWidgets.QMenu("Module 1", self.btn_gprs_sett)
        module2_menu = QtWidgets.QMenu("Module 2", self.btn_gprs_sett)

        # Создание подменю для МосГаз, МРГ, МОГ, Аксон.online
        mosgaz_menu1 = QtWidgets.QMenu("МосГаз", self.btn_gprs_sett)
        mrg_menu1 = QtWidgets.QMenu("МРГ", self.btn_gprs_sett)
        mog_menu1 = QtWidgets.QMenu("МОГ", self.btn_gprs_sett)
        akson_online_menu1 = QtWidgets.QMenu("Аксон.online", self.btn_gprs_sett)


        mog_menu_felial = QtWidgets.QMenu("Мегафон", self.btn_gprs_sett)
        mog_megafon1_felial1 = QtWidgets.QAction("Коломна", self.btn_gprs_sett)
        mog_megafon1_felial2 = QtWidgets.QAction("Красногорск, Клин", self.btn_gprs_sett)
        mog_megafon1_felial3 = QtWidgets.QAction("Мытищи, Дмитров", self.btn_gprs_sett)
        mog_megafon1_felial4 = QtWidgets.QAction("Ногинск, Балашиха", self.btn_gprs_sett)
        mog_megafon1_felial5 = QtWidgets.QAction("Одинцово, Нарофоминск", self.btn_gprs_sett)
        mog_megafon1_felial6 = QtWidgets.QAction("Подольск, Ступино, Серпухов", self.btn_gprs_sett)

        mog_megafon1_felial1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.14.250.246\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 16006\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial2.triggered.connect(lambda:self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 url 10.7.250.12\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 port 16020\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets\r\n"
                                                                               "\r\n"))
        mog_megafon1_felial3.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.8.250.16\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 16005\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial4.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.10.250.17\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 16008\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial5.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.6.250.22\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 16003\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial6.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.5.250.12\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 16001\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))


        mosgaz_megafon1 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)
        mosgaz_mts1 = QtWidgets.QAction("МТС", self.btn_gprs_sett)
        mrg_megafon1 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)
        akson_online_megafon1 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)

        mosgaz_megafon1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn internet\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 1 login gdata\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 1 pass gdata\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 1 url 85.21.105.194\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 1 port 15000\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets\r\n"
                                                                           "\r\n"))
        mosgaz_mts1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn internet.mts.ru\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 login mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 pass mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 url 85.21.105.194\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 port 15000\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets\r\n"
                                                                       "\r\n"))
        mrg_megafon1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn tele123.msk\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 1 login gdata\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 1 pass gdata\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 1 url 192.168.200.2\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 1 port 15009\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets\r\n"
                                                                        "\r\n"))

        akson_online_megafon1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn internet\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 1 login gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 1 pass gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 1 url akson.online\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 1 port 15009\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets\r\n"
                                                                                 "\r\n"))



        mog_menu_felial.addAction(mog_megafon1_felial1)
        mog_menu_felial.addAction(mog_megafon1_felial2)
        mog_menu_felial.addAction(mog_megafon1_felial3)
        mog_menu_felial.addAction(mog_megafon1_felial4)
        mog_menu_felial.addAction(mog_megafon1_felial5)
        mog_menu_felial.addAction(mog_megafon1_felial6)

        mosgaz_menu1.addAction(mosgaz_megafon1)
        mosgaz_menu1.addAction(mosgaz_mts1)
        mrg_menu1.addAction(mrg_megafon1)
        mog_menu1.addMenu(mog_menu_felial)
        akson_online_menu1.addAction(akson_online_megafon1)

        module1_menu.addMenu(mosgaz_menu1)
        module1_menu.addMenu(mrg_menu1)
        module1_menu.addMenu(mog_menu1)
        module1_menu.addMenu(akson_online_menu1)

        mosgaz_menu2 = QtWidgets.QMenu("МосГаз", self.btn_gprs_sett)
        mrg_menu2 = QtWidgets.QMenu("МРГ", self.btn_gprs_sett)
        mog_menu2 = QtWidgets.QMenu("МОГ", self.btn_gprs_sett)
        akson_online_menu2 = QtWidgets.QMenu("Аксон.online", self.btn_gprs_sett)

        mosgaz_megafon2 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)
        mosgaz_mts2 = QtWidgets.QAction("МТС", self.btn_gprs_sett)
        mrg_megafon2 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)
        akson_online_megafon2 = QtWidgets.QAction("Мегафон", self.btn_gprs_sett)

        mog_menu_felial2 = QtWidgets.QMenu("Мегафон", self.btn_gprs_sett)
        mog_megafon2_felial1 = QtWidgets.QAction("Коломна", self.btn_gprs_sett)
        mog_megafon2_felial2 = QtWidgets.QAction("Красногорск, Клин", self.btn_gprs_sett)
        mog_megafon2_felial3 = QtWidgets.QAction("Мытищи, Дмитров", self.btn_gprs_sett)
        mog_megafon2_felial4 = QtWidgets.QAction("Ногинск, Балашиха", self.btn_gprs_sett)
        mog_megafon2_felial5 = QtWidgets.QAction("Одинцово, Нарофоминск", self.btn_gprs_sett)
        mog_megafon2_felial6 = QtWidgets.QAction("Подольск, Ступино, Серпухов", self.btn_gprs_sett)

        mog_megafon2_felial1.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.14.250.246\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16006\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon2_felial2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.7.250.12\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16020\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon2_felial3.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.8.250.16\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16005\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon2_felial4.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.10.250.17\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16008\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon2_felial5.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.6.250.22\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16003\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))
        mog_megafon2_felial6.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 url 10.5.250.12\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 2 port 16001\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets\r\n"
                                                                                "\r\n"))


        mosgaz_megafon2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn internet\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 2 login gdata\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 2 pass gdata\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 2 url 85.21.105.194\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets 2 port 15000\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets\r\n"
                                                                           "\r\n"))
        mosgaz_mts2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn internet.mts.ru\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 2 login mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 2 pass mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 2 url 85.21.105.194\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 2 port 15000\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets\r\n"
                                                                       "\r\n"))
        mrg_megafon2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn tele123.msk\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 2 login gdata\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 2 pass gdata\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 2 url 192.168.200.2\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets 2 port 15009\r\n"
                                                                        "\r\n"
                                                                       "gprs_sets\r\n"
                                                                        "\r\n"))
        akson_online_megafon2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn internet\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 login gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 pass gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 url akson.online\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 port 15009\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets\r\n"
                                                                                 "\r\n"))

        mog_menu_felial2.addAction(mog_megafon2_felial1)
        mog_menu_felial2.addAction(mog_megafon2_felial2)
        mog_menu_felial2.addAction(mog_megafon2_felial3)
        mog_menu_felial2.addAction(mog_megafon2_felial4)
        mog_menu_felial2.addAction(mog_megafon2_felial5)
        mog_menu_felial2.addAction(mog_megafon2_felial6)


        mosgaz_menu2.addAction(mosgaz_megafon2)
        mosgaz_menu2.addAction(mosgaz_mts2)
        mrg_menu2.addAction(mrg_megafon2)
        mog_menu2.addMenu(mog_menu_felial2)
        akson_online_menu2.addAction(akson_online_megafon2)

        module2_menu.addMenu(mosgaz_menu2)
        module2_menu.addMenu(mrg_menu2)
        module2_menu.addMenu(mog_menu2)
        module2_menu.addMenu(akson_online_menu2)

        menu.addMenu(module1_menu)
        menu.addMenu(module2_menu)

        menu.exec_(QtGui.QCursor.pos())

    def show_corrtype_menu(self):
        menu = QtWidgets.QMenu(self.btn_corrtype)

        corr0_action = QtWidgets.QAction("0  SPG761", self.btn_corrtype)
        corr1_action = QtWidgets.QAction("1  SPG761.1", self.btn_corrtype)
        corr2_action = QtWidgets.QAction("2  SPG761.2", self.btn_corrtype)
        corr3_action = QtWidgets.QAction("3  SPG742", self.btn_corrtype)
        corr4_action = QtWidgets.QAction("4  SPG741", self.btn_corrtype)
        corr5_action = QtWidgets.QAction("5  SPG741.1", self.btn_corrtype)
        corr6_action = QtWidgets.QAction("6  EK260", self.btn_corrtype)
        corr7_action = QtWidgets.QAction("7  EK270", self.btn_corrtype)
        corr8_action = QtWidgets.QAction("8  SEVC-D", self.btn_corrtype)
        corr9_action = QtWidgets.QAction("9  CORUS", self.btn_corrtype)
        corr10_action = QtWidgets.QAction("10 FlowGaz", self.btn_corrtype)
        corr11_action = QtWidgets.QAction("11 GFG(Modbus)", self.btn_corrtype)
        corr12_action = QtWidgets.QAction("12 GFG", self.btn_corrtype)
        corr13_action = QtWidgets.QAction("13 TFG(Modbus)", self.btn_corrtype)
        corr14_action = QtWidgets.QAction("14 TFG", self.btn_corrtype)
        corr15_action = QtWidgets.QAction("15 BK", self.btn_corrtype)
        corr16_action = QtWidgets.QAction("16 TC220", self.btn_corrtype)
        corr17_action = QtWidgets.QAction("17 UVP280.01", self.btn_corrtype)
        corr18_action = QtWidgets.QAction("18 UFG", self.btn_corrtype)
        corr19_action = QtWidgets.QAction("19 EK220", self.btn_corrtype)
        corr20_action = QtWidgets.QAction("20 EK155", self.btn_corrtype)
        corr21_action = QtWidgets.QAction("21 FLOWSIC", self.btn_corrtype)
        corr22_action = QtWidgets.QAction("22 AUTOPILOT", self.btn_corrtype)
        corr23_action = QtWidgets.QAction("23 FLOBOSS103", self.btn_corrtype)
        corr24_action = QtWidgets.QAction("24 EK280", self.btn_corrtype)
        corr25_action = QtWidgets.QAction("25 EK230", self.btn_corrtype)
        corr26_action = QtWidgets.QAction("26 EK290", self.btn_corrtype)
        corr27_action = QtWidgets.QAction("27 UFGPP", self.btn_corrtype)
        corr28_action = QtWidgets.QAction("28 SuperFlow21B", self.btn_corrtype)
        corr29_action = QtWidgets.QAction("29 IRVIS", self.btn_corrtype)
        corr30_action = QtWidgets.QAction("30 Goboi-1m", self.btn_corrtype)
        corr31_action = QtWidgets.QAction("31 miniElcor", self.btn_corrtype)
        corr32_action = QtWidgets.QAction("32 FLOW-XP2", self.btn_corrtype)
        corr33_action = QtWidgets.QAction("33 Ultramag", self.btn_corrtype)
        corr34_action = QtWidgets.QAction("34 FLOW-XP_V4", self.btn_corrtype)
        corr35_action = QtWidgets.QAction("35 Vimpel 500", self.btn_corrtype)

        corr0_action.triggered.connect(lambda: self.send_module_command("corrector type 0\r\nreset\r\n\r\n"))
        corr1_action.triggered.connect(lambda: self.send_module_command("corrector type 1\r\nreset"))
        corr2_action.triggered.connect(lambda: self.send_module_command("corrector type 2\r\nreset"))
        corr3_action.triggered.connect(lambda: self.send_module_command("corrector type 3\r\nreset"))
        corr4_action.triggered.connect(lambda: self.send_module_command("corrector type 4\r\nreset"))
        corr5_action.triggered.connect(lambda: self.send_module_command("corrector type 5\r\nreset"))
        corr6_action.triggered.connect(lambda: self.send_module_command("corrector type 6\r\nreset"))
        corr7_action.triggered.connect(lambda: self.send_module_command("corrector type 7\r\nreset"))
        corr8_action.triggered.connect(lambda: self.send_module_command("corrector type 8\r\nreset"))
        corr9_action.triggered.connect(lambda: self.send_module_command("corrector type 9\r\nreset"))
        corr10_action.triggered.connect(lambda: self.send_module_command("corrector type 10\r\n"
                                                                         "reset\r\n"
                                                                         "\r\n"))

        corr11_action.triggered.connect(lambda: self.send_module_command("corrector type 11\r\nreset"))
        corr12_action.triggered.connect(lambda: self.send_module_command("corrector type 12\r\nreset"))
        corr13_action.triggered.connect(lambda: self.send_module_command("corrector type 13\r\nreset"))
        corr14_action.triggered.connect(lambda: self.send_module_command("corrector type 14\r\nreset"))
        corr15_action.triggered.connect(lambda: self.send_module_command("corrector type 15\r\nreset"))
        corr16_action.triggered.connect(lambda: self.send_module_command("corrector type 16\r\nreset"))
        corr17_action.triggered.connect(lambda: self.send_module_command("corrector type 17\r\nreset"))
        corr18_action.triggered.connect(lambda: self.send_module_command("corrector type 18\r\nreset"))
        corr19_action.triggered.connect(lambda: self.send_module_command("corrector type 19\r\nreset"))
        corr20_action.triggered.connect(lambda: self.send_module_command("corrector type 20\r\nreset"))
        corr21_action.triggered.connect(lambda: self.send_module_command("corrector type 21\r\nreset"))
        corr22_action.triggered.connect(lambda: self.send_module_command("corrector type 22\r\nreset"))
        corr23_action.triggered.connect(lambda: self.send_module_command("corrector type 23\r\nreset"))
        corr24_action.triggered.connect(lambda: self.send_module_command("corrector type 24\r\nreset"))
        corr25_action.triggered.connect(lambda: self.send_module_command("corrector type 25\r\nreset"))
        corr26_action.triggered.connect(lambda: self.send_module_command("corrector type 26\r\nreset"))
        corr27_action.triggered.connect(lambda: self.send_module_command("corrector type 27\r\nreset"))
        corr28_action.triggered.connect(lambda: self.send_module_command("corrector type 28\r\nreset"))
        corr29_action.triggered.connect(lambda: self.send_module_command("corrector type 29\r\nreset"))
        corr30_action.triggered.connect(lambda: self.send_module_command("corrector type 30\r\nreset"))
        corr31_action.triggered.connect(lambda: self.send_module_command("corrector type 31\r\nreset"))
        corr32_action.triggered.connect(lambda: self.send_module_command("corrector type 32\r\nreset"))
        corr33_action.triggered.connect(lambda: self.send_module_command("corrector type 33\r\nreset"))
        corr34_action.triggered.connect(lambda: self.send_module_command("corrector type 34\r\nreset"))
        corr35_action.triggered.connect(lambda: self.send_module_command("corrector type 35\r\nreset"))

        menu.addAction(corr0_action)
        menu.addAction(corr1_action)
        menu.addAction(corr2_action)
        menu.addAction(corr3_action)
        menu.addAction(corr4_action)
        menu.addAction(corr5_action)
        menu.addAction(corr6_action)
        menu.addAction(corr7_action)
        menu.addAction(corr8_action)
        menu.addAction(corr9_action)
        menu.addAction(corr10_action)
        menu.addAction(corr11_action)
        menu.addAction(corr12_action)
        menu.addAction(corr13_action)
        menu.addAction(corr14_action)
        menu.addAction(corr15_action)
        menu.addAction(corr16_action)
        menu.addAction(corr17_action)
        menu.addAction(corr18_action)
        menu.addAction(corr19_action)
        menu.addAction(corr20_action)
        menu.addAction(corr21_action)
        menu.addAction(corr22_action)
        menu.addAction(corr23_action)
        menu.addAction(corr24_action)
        menu.addAction(corr25_action)
        menu.addAction(corr26_action)
        menu.addAction(corr27_action)
        menu.addAction(corr28_action)
        menu.addAction(corr29_action)
        menu.addAction(corr30_action)
        menu.addAction(corr31_action)
        menu.addAction(corr32_action)
        menu.addAction(corr33_action)
        menu.addAction(corr34_action)
        menu.addAction(corr35_action)

        menu.exec_(QtGui.QCursor.pos())

    def show_corrsett_menu(self):
        menu = QtWidgets.QMenu(self.btn_corrsett)

        corr0_action2 = QtWidgets.QAction("0  SPG761", self.btn_corrsett)
        corr1_action2 = QtWidgets.QAction("1  SPG761.1", self.btn_corrsett)
        corr2_action2 = QtWidgets.QAction("2  SPG761.2", self.btn_corrsett)
        corr3_action2 = QtWidgets.QAction("3  SPG742", self.btn_corrsett)
        corr4_action2 = QtWidgets.QAction("4  SPG741", self.btn_corrsett)
        corr5_action2 = QtWidgets.QAction("5  SPG741.1", self.btn_corrsett)
        corr6_action2 = QtWidgets.QAction("6  EK260", self.btn_corrsett)
        corr7_action2 = QtWidgets.QAction("7  EK270", self.btn_corrsett)
        corr8_action2 = QtWidgets.QAction("8  SEVC-D", self.btn_corrsett)
        corr9_action2 = QtWidgets.QAction("9  CORUS", self.btn_corrsett)
        corr10_action2 = QtWidgets.QAction("10 FlowGaz", self.btn_corrsett)
        corr11_action2 = QtWidgets.QAction("11 GFG(Modbus)", self.btn_corrsett)
        corr12_action2 = QtWidgets.QAction("12 GFG", self.btn_corrsett)
        corr13_action2 = QtWidgets.QAction("13 TFG(Modbus)", self.btn_corrsett)
        corr14_action2 = QtWidgets.QAction("14 TFG", self.btn_corrsett)
        corr15_action2 = QtWidgets.QAction("15 BK", self.btn_corrsett)
        corr16_action2 = QtWidgets.QAction("16 TC220", self.btn_corrsett)
        corr17_action2 = QtWidgets.QAction("17 UVP280.01", self.btn_corrsett)
        corr18_action2 = QtWidgets.QAction("18 UFG", self.btn_corrsett)
        corr19_action2 = QtWidgets.QAction("19 EK220", self.btn_corrsett)
        corr20_action2 = QtWidgets.QAction("20 EK155", self.btn_corrsett)
        corr21_action2 = QtWidgets.QAction("21 FLOWSIC", self.btn_corrsett)
        corr22_action2 = QtWidgets.QAction("22 AUTOPILOT", self.btn_corrsett)
        corr23_action2 = QtWidgets.QAction("23 FLOBOSS103", self.btn_corrsett)
        corr24_action2 = QtWidgets.QAction("24 EK280", self.btn_corrsett)
        corr25_action2 = QtWidgets.QAction("25 EK230", self.btn_corrsett)
        corr26_action2 = QtWidgets.QAction("26 EK290", self.btn_corrsett)
        corr27_action2 = QtWidgets.QAction("27 UFGPP", self.btn_corrsett)
        corr28_action2 = QtWidgets.QAction("28 SuperFlow21B", self.btn_corrsett)
        corr29_action2 = QtWidgets.QAction("29 IRVIS", self.btn_corrsett)
        corr30_action2 = QtWidgets.QAction("30 Goboi-1m", self.btn_corrsett)
        corr31_action2 = QtWidgets.QAction("31 miniElcor", self.btn_corrsett)
        corr32_action2 = QtWidgets.QAction("32 FLOW-XP2", self.btn_corrsett)
        corr33_action2 = QtWidgets.QAction("33 Ultramag", self.btn_corrsett)
        corr34_action2 = QtWidgets.QAction("34 FLOW-XP_V4", self.btn_corrsett)
        corr35_action2 = QtWidgets.QAction("35 Vimpel 500", self.btn_corrsett)

        corr0_action2.triggered.connect(lambda: self.send_module_command("corrector baud 4800\r\n"
                                                                        "corrector spec 1050001014\r\n"
                                                                        "corrector addr 1 \r\n"))
        corr1_action2.triggered.connect(lambda: self.send_module_command("corrector baud 4800\r\n"
                                                                        "corrector spec 1050001014\r\n"
                                                                        "corrector addr 1 \r\n"))
        corr2_action2.triggered.connect(lambda: self.send_module_command("corrector baud 4800\r\n"
                                                                        "corrector spec 1050001014\r\n"
                                                                        "corrector addr 1 \r\n"))
        corr3_action2.triggered.connect(lambda: self.send_module_command("corrector baud 19200\r\n"))
        corr4_action2.triggered.connect(lambda: self.send_module_command("corrector baud 2400\r\n"))
        corr5_action2.triggered.connect(lambda: self.send_module_command("corrector baud 2400\r\n"))
        corr6_action2.triggered.connect(lambda: self.send_module_command("corrector baud 19200\r\n\r\n"
                                                                        "corrector init 19200\r\n\r\n"
                                                                        "corrector work 19200\r\n"
                                                                         "\r\n"
                                                                        "corrector consumer 00000000\r\n"
                                                                         "\r\n"
                                                                        "corrector supplier 00000000\r\n"
                                                                         "\r\n"))
        corr7_action2.triggered.connect(lambda: self.send_module_command("corrector baud 19200\r\n\r\n"
                                                                        "corrector init 19200\r\n\r\n"
                                                                        "corrector work 19200\r\n"
                                                                         "\r\n"
                                                                        "corrector consumer 00000000\r\n"
                                                                         "\r\n"
                                                                        "corrector supplier 00000000\r\n"
                                                                         "\r\n"))
        corr8_action2.triggered.connect(lambda: self.send_module_command("corrector baud 9600\r\n\r\n"
                                                                        "corrector init 9600\r\n\r\n"
                                                                        "corrector work 9600\r\n\r\n"))
        corr9_action2.triggered.connect(lambda: self.send_module_command("corrector baud 19200\r\n\r\n"
                                                                        "corrector init 19200\r\n\r\n"
                                                                        "corrector work 19200\r\n\r\n"))
        corr10_action2.triggered.connect(lambda: self.send_module_command("corrector baud 2400\r\n"
                                                                         "corrector addr 1\r\n"
                                                                         "\r\n"))
        corr11_action2.triggered.connect(lambda: self.send_module_command(""))
        corr12_action2.triggered.connect(lambda: self.send_module_command(""))
        corr13_action2.triggered.connect(lambda: self.send_module_command(""))
        corr14_action2.triggered.connect(lambda: self.send_module_command(""))
        corr15_action2.triggered.connect(lambda: self.send_module_command("corrector baud 2400\r\n\r\n"
                                                                         "corrector addr 1\r\n\r\n"
                                                                         "corrector fullscan off\r\n\r\n"))
        corr16_action2.triggered.connect(lambda: self.send_module_command("corrector baud 19200\r\n\r\n"
                                                                        "corrector init 19200\r\n\r\n"
                                                                        "corrector work 19200\r\n"
                                                                          "\r\n"
                                                                        "corrector consumer 00000000\r\n"
                                                                          "\r\n"
                                                                        "corrector supplier 00000000\r\n"
                                                                          "\r\n"))
        corr17_action2.triggered.connect(lambda: self.send_module_command(""))
        corr18_action2.triggered.connect(lambda: self.send_module_command(""))
        corr19_action2.triggered.connect(lambda: self.send_module_command(""))
        corr20_action2.triggered.connect(lambda: self.send_module_command(""))
        corr21_action2.triggered.connect(lambda: self.send_module_command("????????????"))
        corr22_action2.triggered.connect(lambda: self.send_module_command(""))
        corr23_action2.triggered.connect(lambda: self.send_module_command(""))
        corr24_action2.triggered.connect(lambda: self.send_module_command(""))
        corr25_action2.triggered.connect(lambda: self.send_module_command(""))
        corr26_action2.triggered.connect(lambda: self.send_module_command(""))
        corr27_action2.triggered.connect(lambda: self.send_module_command(""))
        corr28_action2.triggered.connect(lambda: self.send_module_command(""))
        corr29_action2.triggered.connect(lambda: self.send_module_command("corrector baud 4800\r\n\r\n"
                                                                         "corrector pass 0000\r\n"))
        corr30_action2.triggered.connect(lambda: self.send_module_command(""))
        corr31_action2.triggered.connect(lambda: self.send_module_command(""))
        corr32_action2.triggered.connect(lambda: self.send_module_command(""))
        corr33_action2.triggered.connect(lambda: self.send_module_command(""))
        corr34_action2.triggered.connect(lambda: self.send_module_command(""))
        corr35_action2.triggered.connect(lambda: self.send_module_command(""))

        menu.addAction(corr0_action2)
        menu.addAction(corr1_action2)
        menu.addAction(corr2_action2)
        menu.addAction(corr3_action2)
        menu.addAction(corr4_action2)
        menu.addAction(corr5_action2)
        menu.addAction(corr6_action2)
        menu.addAction(corr7_action2)
        menu.addAction(corr8_action2)
        menu.addAction(corr9_action2)
        menu.addAction(corr10_action2)
        menu.addAction(corr11_action2)
        menu.addAction(corr12_action2)
        menu.addAction(corr13_action2)
        menu.addAction(corr14_action2)
        menu.addAction(corr15_action2)
        menu.addAction(corr16_action2)
        menu.addAction(corr17_action2)
        menu.addAction(corr18_action2)
        menu.addAction(corr19_action2)
        menu.addAction(corr20_action2)
        menu.addAction(corr21_action2)
        menu.addAction(corr22_action2)
        menu.addAction(corr23_action2)
        menu.addAction(corr24_action2)
        menu.addAction(corr25_action2)
        menu.addAction(corr26_action2)
        menu.addAction(corr27_action2)
        menu.addAction(corr28_action2)
        menu.addAction(corr29_action2)
        menu.addAction(corr30_action2)
        menu.addAction(corr31_action2)
        menu.addAction(corr32_action2)
        menu.addAction(corr33_action2)
        menu.addAction(corr34_action2)
        menu.addAction(corr35_action2)

        menu.exec_(QtGui.QCursor.pos())

    def show_portsett_menu(self):
        menu = QtWidgets.QMenu(self.btn_portsets)

        com_menu = QtWidgets.QMenu("Com", self.btn_portsets)
        slot1_menu = QtWidgets.QMenu("Slot 1", self.btn_portsets)
        x4_menu = QtWidgets.QMenu("X4", self.btn_portsets)
        slot2_menu = QtWidgets.QMenu("Slot 2", self.btn_portsets)

        speed_menu0 = QtWidgets.QMenu("Скорость", self.btn_portsets)
        rs_menu0 = QtWidgets.QMenu("Тип", self.btn_portsets)
        parity_menu0 = QtWidgets.QMenu("Четность", self.btn_portsets)
        cross_menu0 = QtWidgets.QMenu("Кросс режим", self.btn_portsets)

        speed0_action1 = QtWidgets.QAction("300", self.btn_portsets)
        speed0_action2 = QtWidgets.QAction("600", self.btn_portsets)
        speed0_action3 = QtWidgets.QAction("1200", self.btn_portsets)
        speed0_action4 = QtWidgets.QAction("2400", self.btn_portsets)
        speed0_action5 = QtWidgets.QAction("4800", self.btn_portsets)
        speed0_action6 = QtWidgets.QAction("9600", self.btn_portsets)
        speed0_action7 = QtWidgets.QAction("19200", self.btn_portsets)
        speed0_action8 = QtWidgets.QAction("38400", self.btn_portsets)
        speed0_action9 = QtWidgets.QAction("57600", self.btn_portsets)
        speed0_action10 = QtWidgets.QAction("115200", self.btn_portsets)

        speed0_action1.triggered.connect(lambda: self.send_module_command("port_sets 0 b 300\r\n"))
        speed0_action2.triggered.connect(lambda: self.send_module_command("port_sets 0 b 600\r\n"))
        speed0_action3.triggered.connect(lambda: self.send_module_command("port_sets 0 b 1200\r\n"))
        speed0_action4.triggered.connect(lambda: self.send_module_command("port_sets 0 b 2400\r\n"))
        speed0_action5.triggered.connect(lambda: self.send_module_command("port_sets 0 b 4800\r\n"))
        speed0_action6.triggered.connect(lambda: self.send_module_command("port_sets 0 b 9600\r\n"))
        speed0_action7.triggered.connect(lambda: self.send_module_command("port_sets 0 b 19200\r\n"))
        speed0_action8.triggered.connect(lambda: self.send_module_command("port_sets 0 b 38400\r\n"))
        speed0_action9.triggered.connect(lambda: self.send_module_command("port_sets 0 b 57600\r\n"))
        speed0_action10.triggered.connect(lambda: self.send_module_command("port_sets 0 b 115200\r\n"))

        rs0_action1 = QtWidgets.QAction("rs 232", self.btn_portsets)
        rs0_action2 = QtWidgets.QAction("rs 422", self.btn_portsets)
        rs0_action3 = QtWidgets.QAction("rs 485", self.btn_portsets)

        rs0_action1.triggered.connect(lambda: self.send_module_command("port_sets 0 rs 232\r\n"))
        rs0_action2.triggered.connect(lambda: self.send_module_command("port_sets 0 rs 422\r\n"))
        rs0_action3.triggered.connect(lambda: self.send_module_command("port_sets 0 rs 485\r\n"))

        parity0_menu_for_speed_8n1 = QtWidgets.QMenu("8n1", self.btn_portsets)
        parity0_menu_for_speed_7e1 = QtWidgets.QMenu("7e1", self.btn_portsets)

        parity0_action1_for_8n1 = QtWidgets.QAction("300", self.btn_portsets)
        parity0_action2_for_8n1 = QtWidgets.QAction("600", self.btn_portsets)
        parity0_action3_for_8n1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity0_action4_for_8n1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity0_action5_for_8n1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity0_action6_for_8n1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity0_action7_for_8n1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity0_action8_for_8n1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity0_action9_for_8n1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity0_action10_for_8n1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity0_action1_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 300 8n1\r\n"))
        parity0_action2_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 600 8n1\r\n"))
        parity0_action3_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 1200 8n1\r\n"))
        parity0_action4_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 2400 8n1\r\n"))
        parity0_action5_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 4800 8n1\r\n"))
        parity0_action6_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 9600 8n1\r\n"))
        parity0_action7_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 19200 8n1\r\n"))
        parity0_action8_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 38400 8n1\r\n"))
        parity0_action9_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 57600 8n1\r\n"))
        parity0_action10_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 0 115200 8n1\r\n"))

        parity0_action1_for_7e1 = QtWidgets.QAction("300", self.btn_portsets)
        parity0_action2_for_7e1 = QtWidgets.QAction("600", self.btn_portsets)
        parity0_action3_for_7e1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity0_action4_for_7e1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity0_action5_for_7e1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity0_action6_for_7e1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity0_action7_for_7e1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity0_action8_for_7e1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity0_action9_for_7e1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity0_action10_for_7e1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity0_action1_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 300 7e1\r\n"))
        parity0_action2_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 600 7e1\r\n"))
        parity0_action3_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 1200 7e1\r\n"))
        parity0_action4_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 2400 7e1\r\n"))
        parity0_action5_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 4800 7e1\r\n"))
        parity0_action6_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 9600 7e1\r\n"))
        parity0_action7_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 19200 7e1\r\n"))
        parity0_action8_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 38400 7e1\r\n"))
        parity0_action9_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 57600 7e1\r\n"))
        parity0_action10_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 0 115200 7e1\r\n"))

        cross0_action1 = QtWidgets.QAction("Включить",self.btn_portsets)
        cross0_action2 = QtWidgets.QAction("Выключить",self.btn_portsets)

        cross0_action1.triggered.connect(lambda: self.send_module_command("port_sets 0 cross"))
        cross0_action2.triggered.connect(lambda: self.send_module_command("port_sets 0 con"))

        cross_menu0.addAction(cross0_action1)
        cross_menu0.addAction(cross0_action2)

        rs_menu0.addAction(rs0_action1)
        rs_menu0.addAction(rs0_action2)
        rs_menu0.addAction(rs0_action3)

        parity0_menu_for_speed_7e1.addAction(parity0_action1_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action2_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action3_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action4_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action5_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action6_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action7_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action8_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action9_for_7e1)
        parity0_menu_for_speed_7e1.addAction(parity0_action10_for_7e1)

        parity0_menu_for_speed_8n1.addAction(parity0_action1_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action2_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action3_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action4_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action5_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action6_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action7_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action8_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action9_for_8n1)
        parity0_menu_for_speed_8n1.addAction(parity0_action10_for_8n1)

        parity_menu0.addMenu(parity0_menu_for_speed_8n1)
        parity_menu0.addMenu(parity0_menu_for_speed_7e1)

        speed_menu0.addAction(speed0_action1)
        speed_menu0.addAction(speed0_action2)
        speed_menu0.addAction(speed0_action3)
        speed_menu0.addAction(speed0_action4)
        speed_menu0.addAction(speed0_action5)
        speed_menu0.addAction(speed0_action6)
        speed_menu0.addAction(speed0_action7)
        speed_menu0.addAction(speed0_action8)
        speed_menu0.addAction(speed0_action9)
        speed_menu0.addAction(speed0_action10)

        com_menu.addMenu(speed_menu0)
        com_menu.addMenu(rs_menu0)
        com_menu.addMenu(parity_menu0)
        com_menu.addMenu(cross_menu0)


        speed_menu1 = QtWidgets.QMenu("Скорость", self.btn_portsets)
        rs_menu1 = QtWidgets.QMenu("Тип", self.btn_portsets)
        parity_menu1 = QtWidgets.QMenu("Четность", self.btn_portsets)

        speed1_action1 = QtWidgets.QAction("300", self.btn_portsets)
        speed1_action2 = QtWidgets.QAction("600", self.btn_portsets)
        speed1_action3 = QtWidgets.QAction("1200", self.btn_portsets)
        speed1_action4 = QtWidgets.QAction("2400", self.btn_portsets)
        speed1_action5 = QtWidgets.QAction("4800", self.btn_portsets)
        speed1_action6 = QtWidgets.QAction("9600", self.btn_portsets)
        speed1_action7 = QtWidgets.QAction("19200", self.btn_portsets)
        speed1_action8 = QtWidgets.QAction("38400", self.btn_portsets)
        speed1_action9 = QtWidgets.QAction("57600", self.btn_portsets)
        speed1_action10 = QtWidgets.QAction("115200", self.btn_portsets)

        speed1_action1.triggered.connect(lambda: self.send_module_command("port_sets 1 b 300\r\n"))
        speed1_action2.triggered.connect(lambda: self.send_module_command("port_sets 1 b 600\r\n"))
        speed1_action3.triggered.connect(lambda: self.send_module_command("port_sets 1 b 1200\r\n"))
        speed1_action4.triggered.connect(lambda: self.send_module_command("port_sets 1 b 2400\r\n"))
        speed1_action5.triggered.connect(lambda: self.send_module_command("port_sets 1 b 4800\r\n"))
        speed1_action6.triggered.connect(lambda: self.send_module_command("port_sets 1 b 9600\r\n"))
        speed1_action7.triggered.connect(lambda: self.send_module_command("port_sets 1 b 19200\r\n"))
        speed1_action8.triggered.connect(lambda: self.send_module_command("port_sets 1 b 38400\r\n"))
        speed1_action9.triggered.connect(lambda: self.send_module_command("port_sets 1 b 57600\r\n"))
        speed1_action10.triggered.connect(lambda: self.send_module_command("port_sets 1 b 115200\r\n"))

        rs1_action1 = QtWidgets.QAction("rs 232", self.btn_portsets)
        rs1_action2 = QtWidgets.QAction("rs 422", self.btn_portsets)
        rs1_action3 = QtWidgets.QAction("rs 485", self.btn_portsets)

        rs1_action1.triggered.connect(lambda: self.send_module_command("port_sets 1 rs 232\r\n"))
        rs1_action2.triggered.connect(lambda: self.send_module_command("port_sets 1 rs 422\r\n"))
        rs1_action3.triggered.connect(lambda: self.send_module_command("port_sets 1 rs 485\r\n"))

        parity1_menu_for_speed_8n1 = QtWidgets.QMenu("8n1", self.btn_portsets)
        parity1_menu_for_speed_7e1 = QtWidgets.QMenu("7e1", self.btn_portsets)

        parity1_action1_for_8n1 = QtWidgets.QAction("300", self.btn_portsets)
        parity1_action2_for_8n1 = QtWidgets.QAction("600", self.btn_portsets)
        parity1_action3_for_8n1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity1_action4_for_8n1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity1_action5_for_8n1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity1_action6_for_8n1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity1_action7_for_8n1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity1_action8_for_8n1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity1_action9_for_8n1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity1_action10_for_8n1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity1_action1_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 300 8n1\r\n"))
        parity1_action2_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 600 8n1\r\n"))
        parity1_action3_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 1200 8n1\r\n"))
        parity1_action4_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 2400 8n1\r\n"))
        parity1_action5_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 4800 8n1\r\n"))
        parity1_action6_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 9600 8n1\r\n"))
        parity1_action7_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 19200 8n1\r\n"))
        parity1_action8_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 38400 8n1\r\n"))
        parity1_action9_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 57600 8n1\r\n"))
        parity1_action10_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 1 115200 8n1\r\n"))

        parity1_action1_for_7e1 = QtWidgets.QAction("300", self.btn_portsets)
        parity1_action2_for_7e1 = QtWidgets.QAction("600", self.btn_portsets)
        parity1_action3_for_7e1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity1_action4_for_7e1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity1_action5_for_7e1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity1_action6_for_7e1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity1_action7_for_7e1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity1_action8_for_7e1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity1_action9_for_7e1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity1_action10_for_7e1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity1_action1_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 300 7e1\r\n"))
        parity1_action2_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 600 7e1\r\n"))
        parity1_action3_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 1200 7e1\r\n"))
        parity1_action4_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 2400 7e1\r\n"))
        parity1_action5_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 4800 7e1\r\n"))
        parity1_action6_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 9600 7e1\r\n"))
        parity1_action7_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 19200 7e1\r\n"))
        parity1_action8_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 38400 7e1\r\n"))
        parity1_action9_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 57600 7e1\r\n"))
        parity1_action10_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 1 115200 7e1\r\n"))

        rs_menu1.addAction(rs1_action1)
        rs_menu1.addAction(rs1_action2)
        rs_menu1.addAction(rs1_action3)

        parity1_menu_for_speed_7e1.addAction(parity1_action1_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action2_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action3_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action4_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action5_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action6_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action7_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action8_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action9_for_7e1)
        parity1_menu_for_speed_7e1.addAction(parity1_action10_for_7e1)

        parity1_menu_for_speed_8n1.addAction(parity1_action1_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action2_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action3_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action4_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action5_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action6_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action7_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action8_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action9_for_8n1)
        parity1_menu_for_speed_8n1.addAction(parity1_action10_for_8n1)

        parity_menu1.addMenu(parity1_menu_for_speed_8n1)
        parity_menu1.addMenu(parity1_menu_for_speed_7e1)

        speed_menu1.addAction(speed1_action1)
        speed_menu1.addAction(speed1_action2)
        speed_menu1.addAction(speed1_action3)
        speed_menu1.addAction(speed1_action4)
        speed_menu1.addAction(speed1_action5)
        speed_menu1.addAction(speed1_action6)
        speed_menu1.addAction(speed1_action7)
        speed_menu1.addAction(speed1_action8)
        speed_menu1.addAction(speed1_action9)
        speed_menu1.addAction(speed1_action10)

        slot1_menu.addMenu(speed_menu1)
        slot1_menu.addMenu(rs_menu1)
        slot1_menu.addMenu(parity_menu1)


        speed_menu2 = QtWidgets.QMenu("Скорость", self.btn_portsets)
        rs_menu2 = QtWidgets.QMenu("Тип", self.btn_portsets)
        parity_menu2 = QtWidgets.QMenu("Четность", self.btn_portsets)
        cross_menu2 = QtWidgets.QMenu("Кросс режим", self.btn_portsets)

        speed2_action1 = QtWidgets.QAction("300", self.btn_portsets)
        speed2_action2 = QtWidgets.QAction("600", self.btn_portsets)
        speed2_action3 = QtWidgets.QAction("1200", self.btn_portsets)
        speed2_action4 = QtWidgets.QAction("2400", self.btn_portsets)
        speed2_action5 = QtWidgets.QAction("4800", self.btn_portsets)
        speed2_action6 = QtWidgets.QAction("9600", self.btn_portsets)
        speed2_action7 = QtWidgets.QAction("19200", self.btn_portsets)
        speed2_action8 = QtWidgets.QAction("38400", self.btn_portsets)
        speed2_action9 = QtWidgets.QAction("57600", self.btn_portsets)
        speed2_action10 = QtWidgets.QAction("115200", self.btn_portsets)

        speed2_action1.triggered.connect(lambda: self.send_module_command("port_sets 2 b 300\r\n"))
        speed2_action2.triggered.connect(lambda: self.send_module_command("port_sets 2 b 600\r\n"))
        speed2_action3.triggered.connect(lambda: self.send_module_command("port_sets 2 b 1200\r\n"))
        speed2_action4.triggered.connect(lambda: self.send_module_command("port_sets 2 b 2400\r\n"))
        speed2_action5.triggered.connect(lambda: self.send_module_command("port_sets 2 b 4800\r\n"))
        speed2_action6.triggered.connect(lambda: self.send_module_command("port_sets 2 b 9600\r\n"))
        speed2_action7.triggered.connect(lambda: self.send_module_command("port_sets 2 b 19200\r\n"))
        speed2_action8.triggered.connect(lambda: self.send_module_command("port_sets 2 b 38400\r\n"))
        speed2_action9.triggered.connect(lambda: self.send_module_command("port_sets 2 b 57600\r\n"))
        speed2_action10.triggered.connect(lambda: self.send_module_command("port_sets 2 b 115200\r\n"))

        rs2_action1 = QtWidgets.QAction("rs 232", self.btn_portsets)
        rs2_action2 = QtWidgets.QAction("rs 422", self.btn_portsets)
        rs2_action3 = QtWidgets.QAction("rs 485", self.btn_portsets)

        rs2_action1.triggered.connect(lambda: self.send_module_command("port_sets 2 rs 232\r\n"))
        rs2_action2.triggered.connect(lambda: self.send_module_command("port_sets 2 rs 422\r\n"))
        rs2_action3.triggered.connect(lambda: self.send_module_command("port_sets 2 rs 485\r\n"))

        parity2_menu_for_speed_8n1 = QtWidgets.QMenu("8n1", self.btn_portsets)
        parity2_menu_for_speed_7e1 = QtWidgets.QMenu("7e1", self.btn_portsets)

        parity2_action1_for_8n1 = QtWidgets.QAction("300", self.btn_portsets)
        parity2_action2_for_8n1 = QtWidgets.QAction("600", self.btn_portsets)
        parity2_action3_for_8n1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity2_action4_for_8n1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity2_action5_for_8n1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity2_action6_for_8n1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity2_action7_for_8n1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity2_action8_for_8n1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity2_action9_for_8n1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity2_action10_for_8n1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity2_action1_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 300 8n1\r\n"))
        parity2_action2_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 600 8n1\r\n"))
        parity2_action3_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 1200 8n1\r\n"))
        parity2_action4_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 2400 8n1\r\n"))
        parity2_action5_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 4800 8n1\r\n"))
        parity2_action6_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 9600 8n1\r\n"))
        parity2_action7_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 19200 8n1\r\n"))
        parity2_action8_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 38400 8n1\r\n"))
        parity2_action9_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 57600 8n1\r\n"))
        parity2_action10_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 2 115200 8n1\r\n"))

        parity2_action1_for_7e1 = QtWidgets.QAction("300", self.btn_portsets)
        parity2_action2_for_7e1 = QtWidgets.QAction("600", self.btn_portsets)
        parity2_action3_for_7e1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity2_action4_for_7e1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity2_action5_for_7e1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity2_action6_for_7e1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity2_action7_for_7e1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity2_action8_for_7e1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity2_action9_for_7e1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity2_action10_for_7e1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity2_action1_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 300 7e1\r\n"))
        parity2_action2_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 600 7e1\r\n"))
        parity2_action3_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 1200 7e1\r\n"))
        parity2_action4_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 2400 7e1\r\n"))
        parity2_action5_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 4800 7e1\r\n"))
        parity2_action6_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 9600 7e1\r\n"))
        parity2_action7_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 19200 7e1\r\n"))
        parity2_action8_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 38400 7e1\r\n"))
        parity2_action9_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 57600 7e1\r\n"))
        parity2_action10_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 2 115200 7e1\r\n"))



        rs_menu2.addAction(rs2_action1)
        rs_menu2.addAction(rs2_action2)
        rs_menu2.addAction(rs2_action3)

        parity2_menu_for_speed_7e1.addAction(parity2_action1_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action2_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action3_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action4_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action5_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action6_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action7_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action8_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action9_for_7e1)
        parity2_menu_for_speed_7e1.addAction(parity2_action10_for_7e1)

        parity2_menu_for_speed_8n1.addAction(parity2_action1_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action2_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action3_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action4_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action5_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action6_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action7_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action8_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action9_for_8n1)
        parity2_menu_for_speed_8n1.addAction(parity2_action10_for_8n1)

        parity_menu2.addMenu(parity2_menu_for_speed_8n1)
        parity_menu2.addMenu(parity2_menu_for_speed_7e1)

        speed_menu2.addAction(speed2_action1)
        speed_menu2.addAction(speed2_action2)
        speed_menu2.addAction(speed2_action3)
        speed_menu2.addAction(speed2_action4)
        speed_menu2.addAction(speed2_action5)
        speed_menu2.addAction(speed2_action6)
        speed_menu2.addAction(speed2_action7)
        speed_menu2.addAction(speed2_action8)
        speed_menu2.addAction(speed2_action9)
        speed_menu2.addAction(speed2_action10)

        x4_menu.addMenu(speed_menu2)
        x4_menu.addMenu(rs_menu2)
        x4_menu.addMenu(parity_menu2)


        speed_menu3 = QtWidgets.QMenu("Скорость", self.btn_portsets)
        rs_menu3 = QtWidgets.QMenu("Тип", self.btn_portsets)
        parity_menu3 = QtWidgets.QMenu("Четность", self.btn_portsets)

        speed3_action1 = QtWidgets.QAction("300", self.btn_portsets)
        speed3_action2 = QtWidgets.QAction("600", self.btn_portsets)
        speed3_action3 = QtWidgets.QAction("1200", self.btn_portsets)
        speed3_action4 = QtWidgets.QAction("2400", self.btn_portsets)
        speed3_action5 = QtWidgets.QAction("4800", self.btn_portsets)
        speed3_action6 = QtWidgets.QAction("9600", self.btn_portsets)
        speed3_action7 = QtWidgets.QAction("19200", self.btn_portsets)
        speed3_action8 = QtWidgets.QAction("38400", self.btn_portsets)
        speed3_action9 = QtWidgets.QAction("57600", self.btn_portsets)
        speed3_action10 = QtWidgets.QAction("115200", self.btn_portsets)

        speed3_action1.triggered.connect(lambda: self.send_module_command("port_sets 3 b 300\r\n"))
        speed3_action2.triggered.connect(lambda: self.send_module_command("port_sets 3 b 600\r\n"))
        speed3_action3.triggered.connect(lambda: self.send_module_command("port_sets 3 b 1200\r\n"))
        speed3_action4.triggered.connect(lambda: self.send_module_command("port_sets 3 b 2400\r\n"))
        speed3_action5.triggered.connect(lambda: self.send_module_command("port_sets 3 b 4800\r\n"))
        speed3_action6.triggered.connect(lambda: self.send_module_command("port_sets 3 b 9600\r\n"))
        speed3_action7.triggered.connect(lambda: self.send_module_command("port_sets 3 b 19200\r\n"))
        speed3_action8.triggered.connect(lambda: self.send_module_command("port_sets 3 b 38400\r\n"))
        speed3_action9.triggered.connect(lambda: self.send_module_command("port_sets 3 b 57600\r\n"))
        speed3_action10.triggered.connect(lambda: self.send_module_command("port_sets 3 b 115200\r\n"))

        rs3_action1 = QtWidgets.QAction("rs 232", self.btn_portsets)
        rs3_action2 = QtWidgets.QAction("rs 422", self.btn_portsets)
        rs3_action3 = QtWidgets.QAction("rs 485", self.btn_portsets)

        rs3_action1.triggered.connect(lambda: self.send_module_command("port_sets 3 rs 232\r\n"))
        rs3_action2.triggered.connect(lambda: self.send_module_command("port_sets 3 rs 422\r\n"))
        rs3_action3.triggered.connect(lambda: self.send_module_command("port_sets 3 rs 485\r\n"))

        parity3_menu_for_speed_8n1 = QtWidgets.QMenu("8n1", self.btn_portsets)
        parity3_menu_for_speed_7e1 = QtWidgets.QMenu("7e1", self.btn_portsets)

        parity3_action1_for_8n1 = QtWidgets.QAction("300", self.btn_portsets)
        parity3_action2_for_8n1 = QtWidgets.QAction("600", self.btn_portsets)
        parity3_action3_for_8n1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity3_action4_for_8n1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity3_action5_for_8n1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity3_action6_for_8n1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity3_action7_for_8n1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity3_action8_for_8n1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity3_action9_for_8n1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity3_action10_for_8n1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity3_action1_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 300 8n1\r\n"))
        parity3_action2_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 600 8n1\r\n"))
        parity3_action3_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 1200 8n1\r\n"))
        parity3_action4_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 2400 8n1\r\n"))
        parity3_action5_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 4800 8n1\r\n"))
        parity3_action6_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 9600 8n1\r\n"))
        parity3_action7_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 19200 8n1\r\n"))
        parity3_action8_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 38400 8n1\r\n"))
        parity3_action9_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 57600 8n1\r\n"))
        parity3_action10_for_8n1.triggered.connect(lambda: self.send_module_command("port_sets 3 115200 8n1\r\n"))

        parity3_action1_for_7e1 = QtWidgets.QAction("300", self.btn_portsets)
        parity3_action2_for_7e1 = QtWidgets.QAction("600", self.btn_portsets)
        parity3_action3_for_7e1 = QtWidgets.QAction("1200", self.btn_portsets)
        parity3_action4_for_7e1 = QtWidgets.QAction("2400", self.btn_portsets)
        parity3_action5_for_7e1 = QtWidgets.QAction("4800", self.btn_portsets)
        parity3_action6_for_7e1 = QtWidgets.QAction("9600", self.btn_portsets)
        parity3_action7_for_7e1 = QtWidgets.QAction("19200", self.btn_portsets)
        parity3_action8_for_7e1 = QtWidgets.QAction("38400", self.btn_portsets)
        parity3_action9_for_7e1 = QtWidgets.QAction("57600", self.btn_portsets)
        parity3_action10_for_7e1 = QtWidgets.QAction("115200", self.btn_portsets)

        parity3_action1_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 300 7e1\r\n"))
        parity3_action2_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 600 7e1\r\n"))
        parity3_action3_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 1200 7e1\r\n"))
        parity3_action4_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 2400 7e1\r\n"))
        parity3_action5_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 4800 7e1\r\n"))
        parity3_action6_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 9600 7e1\r\n"))
        parity3_action7_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 19200 7e1\r\n"))
        parity3_action8_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 38400 7e1\r\n"))
        parity3_action9_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 57600 7e1\r\n"))
        parity3_action10_for_7e1.triggered.connect(lambda: self.send_module_command("port_sets 3 115200 7e1\r\n"))

        rs_menu3.addAction(rs3_action1)
        rs_menu3.addAction(rs3_action2)
        rs_menu3.addAction(rs3_action3)

        parity3_menu_for_speed_7e1.addAction(parity3_action1_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action2_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action3_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action4_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action5_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action6_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action7_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action8_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action9_for_7e1)
        parity3_menu_for_speed_7e1.addAction(parity3_action10_for_7e1)

        parity3_menu_for_speed_8n1.addAction(parity3_action1_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action2_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action3_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action4_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action5_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action6_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action7_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action8_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action9_for_8n1)
        parity3_menu_for_speed_8n1.addAction(parity3_action10_for_8n1)

        parity_menu3.addMenu(parity3_menu_for_speed_8n1)
        parity_menu3.addMenu(parity3_menu_for_speed_7e1)

        speed_menu3.addAction(speed3_action1)
        speed_menu3.addAction(speed3_action2)
        speed_menu3.addAction(speed3_action3)
        speed_menu3.addAction(speed3_action4)
        speed_menu3.addAction(speed3_action5)
        speed_menu3.addAction(speed3_action6)
        speed_menu3.addAction(speed3_action7)
        speed_menu3.addAction(speed3_action8)
        speed_menu3.addAction(speed3_action9)
        speed_menu3.addAction(speed3_action10)

        slot2_menu.addMenu(speed_menu3)
        slot2_menu.addMenu(rs_menu3)
        slot2_menu.addMenu(parity_menu3)





        menu.addMenu(com_menu)
        menu.addMenu(slot1_menu)
        menu.addMenu(x4_menu)
        menu.addMenu(slot2_menu)

        menu.exec_(QtGui.QCursor.pos())

    def send_module_command(self, command):
        # Отправка команды в консоль
        self.terminal_widget.send_data(command)


