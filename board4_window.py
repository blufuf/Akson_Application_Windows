from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import subprocess
import serial
from PyQt5.QtCore import QTimer
import sys, os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
def resource_path(relative_path):
    """Возвращает корректный путь к файлу (работает и в exe, и в IDE)."""
    try:
        base_path = sys._MEIPASS  # временная папка PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Ui_board4_window(object):
    def setupUi(self, board4_window):

        board4_window.setObjectName("board4_window")
        board4_window.setFixedSize(1600, 910)
        board4_window.setStyleSheet("background-color: rgb(168, 168, 168);")

        icon_path = resource_path("AksonICON.ico")
        board4_window.setWindowIcon(QtGui.QIcon(icon_path))

        self.centralwidget = QtWidgets.QWidget(board4_window)
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

        self.text_ip1 = QtWidgets.QPushButton(self.data_window)
        self.text_ip1.setGeometry(QtCore.QRect(0, 40, 190, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.text_ip1.setFont(font)
        self.text_ip1.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.text_ip1.setObjectName("text_ip1")
        self.text_ip1.setText("ifconfig IP")


        self.textip2 = QtWidgets.QPushButton(self.data_window)
        self.textip2.setGeometry(QtCore.QRect(0, 80, 190, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.textip2.setFont(font)
        self.textip2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.textip2.setObjectName("textip2")
        self.textip2.setText("ifconfig MAC")

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

        self.line_ip = QtWidgets.QLineEdit(self.data_window)
        self.line_ip.setGeometry(QtCore.QRect(190, 40, 520, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.line_ip.setFont(font)
        self.line_ip.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.line_ip.setText("")
        self.line_ip.setObjectName("line_ip")
        self.line_ip.setPlaceholderText("X.X.X.X")

        self.line_mac = QtWidgets.QLineEdit(self.data_window)
        self.line_mac.setGeometry(QtCore.QRect(190, 80, 520, 38))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.line_mac.setFont(font)
        self.line_mac.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.line_mac.setText("")
        self.line_mac.setObjectName("line_mac")
        self.line_mac.setPlaceholderText("XX:XX:XX:XX:XX:XX")

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
        self.btn_gprs_sett.setGeometry(QtCore.QRect(320, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_gprs_sett.setFont(font)
        self.btn_gprs_sett.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_gprs_sett.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_gprs_sett.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_gprs_sett.setAutoRaise(False)
        self.btn_gprs_sett.setArrowType(QtCore.Qt.NoArrow)
        self.btn_gprs_sett.setObjectName("btn_gprs_sett")

        self.btn_ifconfig = QtWidgets.QToolButton(self.btn_window)
        self.btn_ifconfig.setGeometry(QtCore.QRect(540, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_ifconfig.setFont(font)
        self.btn_ifconfig.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_ifconfig.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_ifconfig.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_ifconfig.setAutoRaise(False)
        self.btn_ifconfig.setArrowType(QtCore.Qt.NoArrow)
        self.btn_ifconfig.setObjectName("btn_ifconfig")
        self.btn_ifconfig.setText("Настройка\nifconfig")

        self.btn_ifconfig_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_ifconfig_check.setGeometry(QtCore.QRect(460, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_ifconfig_check.setFont(font)
        self.btn_ifconfig_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_ifconfig_check.setObjectName("btn_ifconfig_check")
        self.btn_ifconfig_check.setText("Проверка\nifconfig")

        self.btn_gprs_sett_check = QtWidgets.QPushButton(self.btn_window)
        self.btn_gprs_sett_check.setGeometry(QtCore.QRect(240, 40, 82, 70))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_gprs_sett_check.setFont(font)
        self.btn_gprs_sett_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_gprs_sett_check.setObjectName("btn_gprs_sett_check")


        self.btn_portsets_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_portsets_check.setGeometry(QtCore.QRect(648, 160, 80, 60))
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

        self.btn_update_guid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update_guid.setGeometry(QtCore.QRect(740, 20, 137, 81))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_update_guid.setFont(font)
        self.btn_update_guid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_update_guid.setObjectName("btn_update_guid")

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

        self.btn_sys_sensors = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sys_sensors.setGeometry(QtCore.QRect(400, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_sys_sensors.setFont(font)
        self.btn_sys_sensors.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_sys_sensors.setObjectName("btn_sys_sensors")

        self.btn_aiinfo_time = QtWidgets.QPushButton(self.centralwidget)
        self.btn_aiinfo_time.setGeometry(QtCore.QRect(177, 160, 137, 60))
        font = QtGui.QFont()
        font.setPointSize(10.0)
        self.btn_aiinfo_time.setFont(font)
        self.btn_aiinfo_time.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_aiinfo_time.setObjectName("btn_aiinfo_time")
        self.btn_aiinfo_time.setText("Повторять\nai_info")

        self.btn_aiinfo_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_aiinfo_check.setGeometry(QtCore.QRect(20, 160, 137, 60))
        font = QtGui.QFont()
        font.setPointSize(10.0)
        self.btn_aiinfo_check.setFont(font)
        self.btn_aiinfo_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_aiinfo_check.setObjectName("btn_aiinfo_check")
        self.btn_aiinfo_check.setText("Проверка\nai_info")

        self.btn_diinfo_time = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diinfo_time.setGeometry(QtCore.QRect(491, 160, 137, 60))
        font = QtGui.QFont()
        font.setPointSize(10.0)
        self.btn_diinfo_time.setFont(font)
        self.btn_diinfo_time.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_diinfo_time.setObjectName("btn_diinfo_time")
        self.btn_diinfo_time.setText("Повторять\ndi_info")

        self.btn_diinfo_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_diinfo_check.setGeometry(QtCore.QRect(334, 160, 137, 60))
        font = QtGui.QFont()
        font.setPointSize(10.0)
        self.btn_diinfo_check.setFont(font)
        self.btn_diinfo_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_diinfo_check.setObjectName("btn_diinfo_check")
        self.btn_diinfo_check.setText("Проверка\ndi_info")

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

        ########################################
        self.aidiset_frame = QtWidgets.QFrame(self.btn_window)
        self.aidiset_frame.setGeometry(QtCore.QRect(10, 140, 421, 421))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.aidiset_frame.setStyleSheet("background-color:rgb(168, 168, 168);")
        self.aidiset_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aidiset_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aidiset_frame.setObjectName("aidiset_frame")

        self.btn_disets_check = QtWidgets.QPushButton(self.aidiset_frame)
        self.btn_disets_check.setGeometry(QtCore.QRect(10, 10, 91, 61))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_disets_check.setFont(font)
        self.btn_disets_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_disets_check.setObjectName("btn_disets_check")
        self.btn_disets_check.setText("Проверка\ndi_sets")

        self.btn_disets = QtWidgets.QPushButton(self.aidiset_frame)
        self.btn_disets.setGeometry(QtCore.QRect(10, 80, 91, 61))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_disets.setFont(font)
        self.btn_disets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_disets.setObjectName("btn_disets")
        self.btn_disets.setText("di_sets")

        self.box_disets_pin = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_disets_pin.setGeometry(QtCore.QRect(100, 10, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_disets_pin.setFont(font)
        self.box_disets_pin.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_disets_pin.setObjectName("box_disets_pin")

        self.box_disets_sid = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_disets_sid.setGeometry(QtCore.QRect(100, 60, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_disets_sid.setFont(font)
        self.box_disets_sid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_disets_sid.setObjectName("box_disets_sid")

        self.box_disets_mid = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_disets_mid.setGeometry(QtCore.QRect(100, 110, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_disets_mid.setFont(font)
        self.box_disets_mid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_disets_mid.setObjectName("box_disets_mid")

        self.btn_aisets_check = QtWidgets.QPushButton(self.aidiset_frame)
        self.btn_aisets_check.setGeometry(QtCore.QRect(10, 170, 91, 61))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_aisets_check.setFont(font)
        self.btn_aisets_check.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_aisets_check.setObjectName("btn_aisets_check")
        self.btn_aisets_check.setText("Проверка\nai_sets")

        self.btn_aisets = QtWidgets.QPushButton(self.aidiset_frame)
        self.btn_aisets.setGeometry(QtCore.QRect(10, 240, 91, 61))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_aisets.setFont(font)
        self.btn_aisets.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_aisets.setObjectName("btn_aisets")
        self.btn_aisets.setText("ai_sets")

        self.box_aisets_pin = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_aisets_pin.setGeometry(QtCore.QRect(100, 170, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_aisets_pin.setFont(font)
        self.box_aisets_pin.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_aisets_pin.setObjectName("box_aisets_pin")

        self.box_aisets_sid = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_aisets_sid.setGeometry(QtCore.QRect(100, 220, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_aisets_sid.setFont(font)
        self.box_aisets_sid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_aisets_sid.setObjectName("box_aisets_sid")

        self.box_aisets_mid = QtWidgets.QComboBox(self.aidiset_frame)
        self.box_aisets_mid.setGeometry(QtCore.QRect(100, 270, 320, 31))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_aisets_mid.setFont(font)
        self.box_aisets_mid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_aisets_mid.setObjectName("box_aisets_mid")

        self.ls_line = QtWidgets.QLineEdit(self.aidiset_frame)
        self.ls_line.setGeometry(QtCore.QRect(100, 320, 170, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.ls_line.setFont(font)
        self.ls_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.ls_line.setPlaceholderText("LS")
        self.ls_line.setObjectName("ls_line")

        self.hs_line = QtWidgets.QLineEdit(self.aidiset_frame)
        self.hs_line.setGeometry(QtCore.QRect(100, 370, 170, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.hs_line.setFont(font)
        self.hs_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.hs_line.setPlaceholderText("HS")
        self.hs_line.setObjectName("hs_line")


        self.btn_aisets_lshs = QtWidgets.QPushButton(self.aidiset_frame)
        self.btn_aisets_lshs.setGeometry(QtCore.QRect(10, 310, 91, 91))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_aisets_lshs.setFont(font)
        self.btn_aisets_lshs.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_aisets_lshs.setObjectName("btn_aisets_lshs")
        self.btn_aisets_lshs.setText("Установить\n"
                                     "LS/HS")

        self.btn_dicts = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dicts.setGeometry(QtCore.QRect(280, 840, 100, 40))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_dicts.setFont(font)
        self.btn_dicts.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_dicts.setObjectName("btn_dicts")
        self.btn_dicts.setText("dicts")



        ############################
        #####1WIRE#####

        self.wire_frame = QtWidgets.QFrame(self.btn_window)
        self.wire_frame.setGeometry(QtCore.QRect(440, 230, 391, 331))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.wire_frame.setStyleSheet("background-color:rgb(168, 168, 168);")
        self.wire_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wire_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wire_frame.setObjectName("wire_frame")

        self.btn_ls1wire = QtWidgets.QPushButton(self.wire_frame)
        self.btn_ls1wire.setGeometry(QtCore.QRect(10, 10, 90,50 ))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_ls1wire.setFont(font)
        self.btn_ls1wire.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_ls1wire.setObjectName("btn_ls1wire")
        self.btn_ls1wire.setText("ls1wire")

        self.btn_1wire_temp = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_temp.setGeometry(QtCore.QRect(100, 10, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_temp.setFont(font)
        self.btn_1wire_temp.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_temp.setObjectName("btn_1wire_temp")
        self.btn_1wire_temp.setText("1wire_temp")

        self.btn_tablets_add = QtWidgets.QPushButton(self.wire_frame)
        self.btn_tablets_add.setGeometry(QtCore.QRect(190, 10, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_tablets_add.setFont(font)
        self.btn_tablets_add.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_tablets_add.setObjectName("btn_tablets_add")
        self.btn_tablets_add.setText("tablets\nadd")

        self.btn_1wire_clear = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_clear.setGeometry(QtCore.QRect(280, 10, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_clear.setFont(font)
        self.btn_1wire_clear.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_clear.setObjectName("btn_1wire_clear")
        self.btn_1wire_clear.setText("1wire_clear")

        self.btn_1wire_add = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_add.setGeometry(QtCore.QRect(10, 60, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_add.setFont(font)
        self.btn_1wire_add.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_add.setObjectName("btn_1wire_add")
        self.btn_1wire_add.setText("1wire_add")

        self.btn_1wire_add_sys = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_add_sys.setGeometry(QtCore.QRect(10, 110, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_add_sys.setFont(font)
        self.btn_1wire_add_sys.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_add_sys.setObjectName("btn_1wire_add_sys")
        self.btn_1wire_add_sys.setText("1wire\nadd system")

        self.btn_1wire_del = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_del.setGeometry(QtCore.QRect(10, 160, 90, 50))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_del.setFont(font)
        self.btn_1wire_del.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_del.setObjectName("btn_1wire_del")
        self.btn_1wire_del.setText("1wire del")

        self.box_1wire_number = QtWidgets.QComboBox(self.wire_frame)
        self.box_1wire_number.setGeometry(QtCore.QRect(100, 70, 260, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_1wire_number.setFont(font)
        self.box_1wire_number.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_1wire_number.setObjectName("box_1wire_number")

        self.box_1wire_aisid = QtWidgets.QComboBox(self.wire_frame)
        self.box_1wire_aisid.setGeometry(QtCore.QRect(100, 120, 260, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.box_1wire_aisid.setFont(font)
        self.box_1wire_aisid.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.box_1wire_aisid.setObjectName("box_1wire_aisid")

        self.wire_del_line = QtWidgets.QLineEdit(self.wire_frame)
        self.wire_del_line.setGeometry(QtCore.QRect(100, 170, 260, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.wire_del_line.setFont(font)
        self.wire_del_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.wire_del_line.setPlaceholderText("#номер датчика для удаления")
        self.wire_del_line.setObjectName("wire_del_line")

        self.btn_1wire_edit = QtWidgets.QPushButton(self.wire_frame)
        self.btn_1wire_edit.setGeometry(QtCore.QRect(10, 220, 90, 90))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.btn_1wire_edit.setFont(font)
        self.btn_1wire_edit.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.btn_1wire_edit.setObjectName("btn_1wire_edit")
        self.btn_1wire_edit.setText("Установить\nLS/HS")

        self.wire_ls_line = QtWidgets.QLineEdit(self.wire_frame)
        self.wire_ls_line.setGeometry(QtCore.QRect(100, 230, 260, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.wire_ls_line.setFont(font)
        self.wire_ls_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.wire_ls_line.setPlaceholderText("LS")
        self.wire_ls_line.setObjectName("wire_ls_line")

        self.wire_hs_line = QtWidgets.QLineEdit(self.wire_frame)
        self.wire_hs_line.setGeometry(QtCore.QRect(100, 280, 260, 30))
        font = QtGui.QFont()
        font.setPointSizeF(10.0)
        self.wire_hs_line.setFont(font)
        self.wire_hs_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.wire_hs_line.setPlaceholderText("HS")
        self.wire_hs_line.setObjectName("wire_hs_line")


        board4_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(board4_window)
        self.statusbar.setObjectName("statusbar")
        board4_window.setStatusBar(self.statusbar)
        self.retranslateUi(board4_window)
        QtCore.QMetaObject.connectSlotsByName(board4_window)




        # Подключаем слоты к кнопкам
        self.btn_datatime.clicked.connect(self.send_datetime_command)
        self.btn_entermoduls.clicked.connect(self.show_module_menu)
        self.btn_gprs_sett.clicked.connect(self.show_gprs_menu)
        self.btn_entermoduls_check.clicked.connect(self.send_modems_sets_command)
        self.btn_gprs_sett_check.clicked.connect(self.send_btn_gprs_sett_check)
        self.btn_settime.clicked.connect(self.send_settime)
        self.btn_update_guid.clicked.connect(self.update_guid_command)
        self.btn_erase_data.clicked.connect(self.send_erase_data)
        self.btn_erase_flash.clicked.connect(self.send_erase_flash)
        self.btn_reset.clicked.connect(self.send_reset)
        self.btn_help.clicked.connect(self.send_help)
        self.btn_portsets_check.clicked.connect(self.send_portsets_check)
        self.btn_ver.clicked.connect(self.send_ver)
        self.btn_sys_sensors.clicked.connect(self.send_sys_sensors)
        self.text_guid.clicked.connect(self.send_general_sets)
        self.btn_timesets.clicked.connect(self.show_timesets)
        self.btn_timesets_check.clicked.connect(self.send_timesets_check)
        self.btn_aiinfo_check.clicked.connect(self.send_aiinfo_check)
        self.btn_diinfo_check.clicked.connect(self.send_diinfo_check)
        self.btn_disets_check.clicked.connect(self.send_disets_check)
        self.btn_aisets_check.clicked.connect(self.send_aisets_check)
        self.btn_aisets_lshs.clicked.connect(self.send_aisets_lshs)
        self.btn_ifconfig_check.clicked.connect(self.send_ifconfig_check)
        self.text_ip1.clicked.connect(self.send_ifconfig_ip)
        self.textip2.clicked.connect(self.send_ifconfig_mac)
        self.btn_ifconfig.clicked.connect(self.show_ifconfig_menu)
        self.btn_dicts.clicked.connect(self.send_dicts)

        self.btn_ls1wire.clicked.connect(self.send_ls1wire)
        self.btn_1wire_temp.clicked.connect(self.send_wire_temp)
        self.btn_tablets_add.clicked.connect(self.send_tablets_add)
        self.btn_1wire_clear.clicked.connect(self.send_wire_temp_clear)
        self.btn_1wire_add.clicked.connect(self.send_wire_temp_add)
        self.btn_1wire_add_sys.clicked.connect(self.send_wire_temp_add_sys)
        self.btn_1wire_del.clicked.connect(self.send_wire_temp_del)
        self.btn_1wire_edit.clicked.connect(self.send_sensor_edit)


        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(3000)  # 3 секунды
        self.timer1.timeout.connect(self.send_periodic_command1)

        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(3000)  # 3 секунды
        self.timer2.timeout.connect(self.send_periodic_command2)

        self.btn_aiinfo_time.clicked.connect(self.send_aiinfo_time)
        self.btn_diinfo_time.clicked.connect(self.send_diinfo_time)

        self.update_timer = QtCore.QTimer()
        QtCore.QTimer.singleShot(5000, self.update_comboboxes)


        self.command_running1 = False
        self.command_running2 = False


        board4_window.closeEvent = self.closeEvent

        self.populate_comboboxes()
        self.populate_comboboxes2()
        self.populate_comboboxes_wire_sid()
        self.btn_disets.clicked.connect(self.send_di_sets_command)
        self.btn_aisets.clicked.connect(self.send_ai_sets_command)

    def retranslateUi(self, board4_window):
        _translate = QtCore.QCoreApplication.translate
        board4_window.setWindowTitle(_translate("board4_window", "АКСОН 1V1 F101/F103"))

        self.btn_entermoduls.setText(_translate("board4_window", "Выбор\n"
        "модема"))
        self.btn_gprs_sett.setText(_translate("board4_window", "Настрой-\nки\nGPRS"))
        self.btn_datatime.setText(_translate("board4_window", "Проверка\ndatatime"))
        self.btn_update_guid.setText(_translate("board4_window", "Установить\n"
        "GUID"))
        self.btn_entermoduls_check.setText(_translate("board4_window", "Про-\nверка"))
        self.btn_gprs_sett_check.setText(_translate("board4_window", "Про-\nверка"))
        self.btn_portsets_check.setText(_translate("board4_window", "port_set\nCheck"))
        self.btn_settime.setText(_translate("board4_window", "Set\ntime"))
        self.btn_erase_data.setText(_translate("board4_window", "Erase Data"))
        self.btn_erase_flash.setText(_translate("board4_window", "Erase Flash"))
        self.btn_reset.setText(_translate("board4_window", "Reset"))
        self.btn_help.setText(_translate("board4_window", "Help"))
        self.btn_ver.setText(_translate("board4_window", "Ver"))
        self.btn_sys_sensors.setText(_translate("Board4_window", "Sys sens"))
        self.text_guid.setText(_translate("Board4_window", "GUID"))
        self.btn_timesets_check.setText(_translate("Board4_window", "Проверка"))
        self.btn_timesets.setText(_translate("Board4_window", "Time\nsets"))



    def send_ls1wire(self):
        self.box_1wire_number.clear()
        self.collected_data = []
        self.terminal_widget.serial_thread.data_received.connect(self.collect_ls1wire_output)
        self.terminal_widget.send_data("ls1wire")
        self.data_collection_timer = QTimer()
        self.data_collection_timer.setSingleShot(True)
        self.data_collection_timer.timeout.connect(self.finish_ls1wire_collection)
        self.data_collection_timer.start(1000)

    def collect_ls1wire_output(self, data):
        print(f"Received data: {data.strip()}")
        self.collected_data.append(data)
        self.data_collection_timer.start(1000)

    def finish_ls1wire_collection(self):
        self.terminal_widget.serial_thread.data_received.disconnect(self.collect_ls1wire_output)
        self.handle_ls1wire_output("\n".join(self.collected_data))

    def handle_ls1wire_output(self, data):
        self.box_1wire_number.clear()
        print(f"Collected data: {data}")
        lines = data.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                parts = line.split()
                if len(parts) > 1:
                    device_id = parts[1]
                    print(f"Adding device ID: {device_id}")
                    self.box_1wire_number.addItem(device_id)

    def send_wire_temp(self):
        self.terminal_widget.send_data("1wire_temp")

    def send_tablets_add(self):
        number = self.box_1wire_number.currentText()

        menu = QtWidgets.QMenu(self.btn_tablets_add)

        tablets_add_action1 = QtWidgets.QAction("tablets add", self.btn_tablets_add)
        tablets_add_action1.triggered.connect(lambda: self.send_module_command(f"tablets add {number}"))
        tablets_action1 = QtWidgets.QAction("tablets", self.btn_tablets_add)
        tablets_action1.triggered.connect(lambda: self.send_module_command("tablets"))

        menu.addAction(tablets_add_action1)
        menu.addAction(tablets_action1)

        menu.exec_(QtGui.QCursor.pos())

    def send_wire_temp_clear(self):
        self.terminal_widget.send_data("1wire_temp clear")

    def send_wire_temp_add(self):
        number = self.box_1wire_number.currentText()
        sid = self.extract_id(self.box_1wire_aisid.currentText())
        self.terminal_widget.send_data(f"1wire_temp add {number} {sid}")

    def send_wire_temp_add_sys(self):
        number = self.box_1wire_number.currentText()
        self.terminal_widget.send_data(f'1wire_temp add {number} sys')

    def send_wire_temp_del(self):
        number = self.wire_del_line.text()
        self.terminal_widget.send_data(f'1wire_temp del {number}')


    def send_sensor_edit(self):
        sid = self.extract_id(self.box_1wire_aisid.currentText())
        ls = self.wire_ls_line.text()
        hs = self.wire_hs_line.text()
        self.terminal_widget.send_data(f'sensor_edit {sid} on {ls} {hs}')

    def populate_comboboxes_wire_sid(self):
        ai_sid_wire = self.load_items_from_file('ai_sid.txt')

        self.box_1wire_aisid.clear()

        self.box_1wire_aisid.addItems(ai_sid_wire)


    def update_comboboxes(self):
        self.populate_comboboxes()
        self.populate_comboboxes2()
        self.populate_comboboxes_wire_sid()

    def send_dicts(self):
        self.terminal_widget.send_data("dicts")

    def show_ifconfig_menu(self):
        menu = QtWidgets.QMenu(self.btn_ifconfig)

        ifconf_default = QtWidgets.QAction("Default", self.btn_ifconfig)
        ifconf_up_down = QtWidgets.QMenu("UP / DOWN", self.btn_ifconfig)
        ifconf_dhcp = QtWidgets.QMenu("DHCP ON / OFF", self.btn_ifconfig)

        ifconf_default.triggered.connect(lambda: self.send_module_command("ifconfig default \r\n"))

        ifconf_up = QtWidgets.QAction("Up", self.btn_ifconfig)
        ifconf_down = QtWidgets.QAction("Down", self.btn_ifconfig)
        ifconf_dhcp_on = QtWidgets.QAction("On", self.btn_ifconfig)
        ifconf_dhcp_off = QtWidgets.QAction("Off", self.btn_ifconfig)

        ifconf_up.triggered.connect(lambda: self.send_module_command("ifconfig up"))
        ifconf_down.triggered.connect(lambda: self.send_module_command("ifconfig down"))
        ifconf_dhcp_on.triggered.connect(lambda: self.send_module_command("ifconfig dhcp on"))
        ifconf_dhcp_off.triggered.connect(lambda: self.send_module_command("ifconfig dhcp off"))

        ifconf_dhcp.addAction(ifconf_dhcp_on)
        ifconf_dhcp.addAction(ifconf_dhcp_off)
        ifconf_up_down.addAction(ifconf_up)
        ifconf_up_down.addAction(ifconf_down)

        menu.addAction(ifconf_default)
        menu.addMenu(ifconf_up_down)
        menu.addMenu(ifconf_dhcp)

        menu.exec_(QtGui.QCursor.pos())


    def send_ifconfig_ip(self):
        ip = self.line_ip.text()
        self.terminal_widget.send_data(f'ifconfig ip {ip}')

    def send_ifconfig_mac(self):
        mac = self.line_mac.text()
        self.terminal_widget.send_data(f'ifconfig mac {mac}')

    def send_ifconfig_check(self):
        self.terminal_widget.send_data("ifconfig")

    def send_aisets_lshs(self):
        pin = self.extract_id(self.box_aisets_pin.currentText())
        ls = self.ls_line.text()
        hs = self.hs_line.text()
        self.terminal_widget.send_data(f'ai_sets p {pin} ls {ls} hs {hs}')

    def load_items_from_file(self, filename):
        items = []
        try:
            with open(resource_path(filename), 'r', encoding='utf-8') as file:
                items = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File {filename} not found.")
            # Убедитесь, что этот вызов не вызывает рекурсию
            # self.update_terminal(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
            # Убедитесь, что этот вызов не вызывает рекурсию
            # self.update_terminal(f"Error loading {filename}: {str(e)}")
        return items

    def populate_comboboxes(self):
        # Загрузка элементов из файлов и добавление в комбобоксы
        di_sid_items = self.load_items_from_file('di_sid.txt')
        di_mid_items = self.load_items_from_file('di_mid.txt')

        self.box_disets_sid.clear()
        self.box_disets_mid.clear()

        self.box_disets_sid.addItems(di_sid_items)
        self.box_disets_mid.addItems(di_mid_items)

        for i in range(20):
            self.box_disets_pin.addItem(str(i))

    def populate_comboboxes2(self):
        # Загрузка элементов из файлов и добавление в комбобоксы
        ai_sid_items = self.load_items_from_file('ai_sid.txt')
        ai_mid_items = self.load_items_from_file('ai_mid.txt')

        self.box_aisets_sid.clear()
        self.box_aisets_mid.clear()

        self.box_aisets_sid.addItems(ai_sid_items)
        self.box_aisets_mid.addItems(ai_mid_items)

        for i in range(16):
            self.box_aisets_pin.addItem(str(i))

    def extract_id(self, text):
        # Extracts the first number within parentheses
        return text.split(' ')[0].strip('()')

    def send_di_sets_command(self):
        pin = self.box_disets_pin.currentText()
        sid = self.extract_id(self.box_disets_sid.currentText())
        mid = self.extract_id(self.box_disets_mid.currentText())

        command = f"di_sets p {pin} sid {sid} mid {mid}"
        self.terminal_widget.send_data(command)

    def send_ai_sets_command(self):
        pin = self.box_aisets_pin.currentText()
        sid = self.extract_id(self.box_aisets_sid.currentText())
        mid = self.extract_id(self.box_aisets_mid.currentText())

        command = f"ai_sets p {pin} sid {sid} mid {mid}"
        self.terminal_widget.send_data(command)


    def send_aisets_check(self):
        self.terminal_widget.send_data('ai_sets')

    def send_disets_check(self):
        self.terminal_widget.send_data('di_sets')

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

    def send_sys_sensors(self):
        self.terminal_widget.send_data('sys_sensors')

    def send_general_sets(self):
        self.terminal_widget.send_data('general_sets')

    def send_periodic_command1(self):
        self.terminal_widget.send_data('ai_info')

    def send_aiinfo_check(self):
        self.terminal_widget.send_data('ai_info')

    def send_aiinfo_time(self):
        if self.command_running1:
            self.timer1.stop()
            self.command_running1 = False
            self.btn_aiinfo_time.setText("ai_info\nВключить")
        else:
            self.timer1.start()
            self.command_running1 = True
            self.btn_aiinfo_time.setText("ai_info\nВыключить")

    def send_periodic_command2(self):
        self.terminal_widget.send_data('di_info')

    def send_diinfo_check(self):
        self.terminal_widget.send_data('di_info')

    def send_diinfo_time(self):
        if self.command_running2:
            self.timer2.stop()
            self.command_running2 = False
            self.btn_diinfo_time.setText("di_info\nВключить")
        else:
            self.timer2.start()
            self.command_running2 = True
            self.btn_diinfo_time.setText("di_info\nВыключить")

    def closeEvent(self, event):
        try:
            self.terminal_widget.stop_serial_thread()  # Закрываем соединение, если это необходимо
            event.accept()
        except Exception as e:
            print(f"Error in closeEvent: {str(e)}")
            event.ignore()

    def send_ver(self):
        self.terminal_widget.send_data('ver')

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

    def send_modems_sets_command(self):
        menu = QtWidgets.QMenu(self.btn_entermoduls_check)

        modemsets_action1 = QtWidgets.QAction("modems_sets", self.btn_entermoduls_check)
        modemsets_action1.triggered.connect(lambda: self.send_module_command("modems_sets"))
        modulessets_action1 = QtWidgets.QAction("modules_sets", self.btn_entermoduls_check)
        modulessets_action1.triggered.connect(lambda: self.send_module_command("modules_sets"))

        menu.addAction(modemsets_action1)
        menu.addAction(modulessets_action1)

        menu.exec_(QtGui.QCursor.pos())

    def send_btn_gprs_sett_check(self):

        menu = QtWidgets.QMenu(self.btn_gprs_sett_check)

        gprs_sets_all_action1 = QtWidgets.QAction("gprs_sets all", self.btn_gprs_sett_check)
        gprs_sets_all_action1.triggered.connect(lambda: self.send_module_command("gprs_sets all"))
        gprs_sets_action1 = QtWidgets.QAction("gprs_sets", self.btn_gprs_sett_check)
        gprs_sets_action1.triggered.connect(lambda: self.send_module_command("gprs_sets"))

        menu.addAction(gprs_sets_all_action1)
        menu.addAction(gprs_sets_action1)

        menu.exec_(QtGui.QCursor.pos())

    def send_datetime_command(self):
        self.terminal_widget.send_data('datetime')

    def update_guid_command(self):
        guid_value = self.line_guid.text()
        self.terminal_widget.send_data(f'general_sets guid {guid_value}')

    def show_module_menu(self):
        # Создание выпадающего меню для кнопки Enter Modules
        menu = QtWidgets.QMenu(self.btn_entermoduls)

        # Создание подменю для Module 1 и Module 2
        module1_menu = QtWidgets.QMenu("modems 1", self.btn_entermoduls)
        module2_menu = QtWidgets.QMenu("modems 2", self.btn_entermoduls)
        module3_menu = QtWidgets.QMenu("modules 1", self.btn_entermoduls)
        module4_menu = QtWidgets.QMenu("modules 2", self.btn_entermoduls)

        # Создание подменю для ON и OFF в каждом Module
        on_menu1 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action1 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action1.triggered.connect(lambda: self.send_module_command("modems_sets 1 off\r\n"
                                                                        "modems_sets"))

        on_menu2 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action2 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action2.triggered.connect(lambda: self.send_module_command("modems_sets 2 off\r\n"
                                                                        "modems_sets"))

        on_menu3 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action3 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action3.triggered.connect(lambda: self.send_module_command("modules_sets 1 off\r\n"
                                                                       "modules_sets"))

        on_menu4 = QtWidgets.QMenu("ON", self.btn_entermoduls)
        off_action4 = QtWidgets.QAction("OFF", self.btn_entermoduls)
        off_action4.triggered.connect(lambda: self.send_module_command("modules_sets 2 off\r\n"
                                                                       "modules_sets"))
        # Добавление команд GPRS, CSD и ALL в подменю ON
        gprs_action1 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action1 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action1 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action1.triggered.connect(lambda: self.send_module_command("modems_sets 1 on\r\n"
                                                                        "modems_sets 1 gprs\r\n"
                                                                        "modems_sets"))
        csd_action1.triggered.connect(lambda: self.send_module_command("modems_sets 1 on\r\n"
                                                                        "modems_sets 1 csd\r\n"
                                                                        "modems_sets"))
        all_action1.triggered.connect(lambda: self.send_module_command("modems_sets 1 on\r\n"
                                                                        "modems_sets 1 all\r\n"
                                                                        "modems_sets"))

        on_menu1.addAction(gprs_action1)
        on_menu1.addAction(csd_action1)
        on_menu1.addAction(all_action1)

        gprs_action2 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action2 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action2 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action2.triggered.connect(lambda: self.send_module_command("modems_sets 2 on\r\n"
                                                                        "modems_sets 2 gprs\r\n"
                                                                        "modems_sets"))

        csd_action2.triggered.connect(lambda: self.send_module_command("modems_sets 2 on\r\n"
                                                                        "modems_sets 2 csd\r\n"
                                                                        "modems_sets"))
        all_action2.triggered.connect(lambda: self.send_module_command("modems_sets 2 on\r\n"
                                                                        "modems_sets 2 all\r\n"
                                                                        "modems_sets"))

        on_menu2.addAction(gprs_action2)
        on_menu2.addAction(csd_action2)
        on_menu2.addAction(all_action2)

        gprs_action3 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action3 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action3 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action3.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 gprs\r\n"
                                                                        "modules_sets"))

        csd_action3.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 csd\r\n"
                                                                        "modules_sets"))
        all_action3.triggered.connect(lambda: self.send_module_command("modules_sets 1 on\r\n"
                                                                        "modules_sets 1 all\r\n"
                                                                        "modules_sets"))
        on_menu3.addAction(gprs_action3)
        on_menu3.addAction(csd_action3)
        on_menu3.addAction(all_action3)

        gprs_action4 = QtWidgets.QAction("GPRS", self.btn_entermoduls)
        csd_action4 = QtWidgets.QAction("CSD", self.btn_entermoduls)
        all_action4 = QtWidgets.QAction("ALL", self.btn_entermoduls)

        gprs_action4.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 gprs\r\n"
                                                                        "modules_sets"))

        csd_action4.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 csd\r\n"
                                                                        "modules_sets"))
        all_action4.triggered.connect(lambda: self.send_module_command("modules_sets 2 on\r\n"
                                                                        "modules_sets 2 all\r\n"
                                                                        "modules_sets"))

        on_menu4.addAction(gprs_action4)
        on_menu4.addAction(csd_action4)
        on_menu4.addAction(all_action4)

        # Добавление подменю ON и OFF в Module 1 и Module 2
        module1_menu.addMenu(on_menu1)
        module1_menu.addAction(off_action1)

        module2_menu.addMenu(on_menu2)
        module2_menu.addAction(off_action2)

        module3_menu.addMenu(on_menu3)
        module3_menu.addAction(off_action3)

        module4_menu.addMenu(on_menu4)
        module4_menu.addAction(off_action4)

        # Добавление Module 1 и Module 2 в основное меню
        menu.addMenu(module1_menu)
        menu.addMenu(module2_menu)
        menu.addMenu(module3_menu)
        menu.addMenu(module4_menu)

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
                                                                                "gprs_sets 1 port 15006\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets all\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial2.triggered.connect(lambda:self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 url 10.7.250.12\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets 1 port 15020\r\n"
                                                                               "\r\n"
                                                                                "gprs_sets all\r\n"
                                                                               "\r\n"))
        mog_megafon1_felial3.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.8.250.16\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 15005\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets all\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial4.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.10.250.17\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 15008\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets all\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial5.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.6.250.22\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 15003\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets all\r\n"
                                                                                "\r\n"))
        mog_megafon1_felial6.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn mosoblgaz.msk\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 login mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 pass mega\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 url 10.5.250.12\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets 1 port 15001\r\n"
                                                                                "\r\n"
                                                                                "gprs_sets all\r\n"
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
                                                                          "gprs_sets 1 port 16000\r\n"
                                                                           "\r\n"
                                                                          "gprs_sets all\r\n"
                                                                           "\r\n"))
        mosgaz_mts1.triggered.connect(lambda: self.send_module_command("gprs_sets 1 apn internet.mts.ru\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 login mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 pass mts\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 url 85.21.105.194\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets 1 port 16000\r\n"
                                                                       "\r\n"
                                                                       "gprs_sets all\r\n"
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
                                                                       "gprs_sets all\r\n"
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
                                                                                 "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                                "gprs_sets all\r\n"
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
                                                                          "gprs_sets all\r\n"
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
                                                                       "gprs_sets all\r\n"
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
                                                                       "gprs_sets all\r\n"
                                                                        "\r\n"))
        akson_online_megafon2.triggered.connect(lambda: self.send_module_command("gprs_sets 2 apn internet\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 login gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 pass gdata\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 url akson.online\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets 2 port 15019\r\n"
                                                                                 "\r\n"
                                                                                 "gprs_sets all\r\n"
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


    def send_module_command(self, command):
        # Отправка команды в консоль
        self.terminal_widget.send_data(command)




