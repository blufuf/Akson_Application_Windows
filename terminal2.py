import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QLineEdit, QApplication, QPushButton, \
    QFileDialog, QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QKeyEvent, QDragEnterEvent, QDropEvent
import time
import subprocess
from tabulate import tabulate
import re
import os
import sys

def resource_path(relative_path):
    """Возвращает путь к ресурсу (работает и в exe, и при запуске из IDE)."""
    try:
        base_path = sys._MEIPASS  # временная папка, куда PyInstaller распаковывает содержимое
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SerialThread2(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.running = False

    def run(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=1)
            self.running = True
            buffer = b""
            while self.running:
                if self.serial_connection.in_waiting > 0:
                    try:
                        data = self.serial_connection.read(self.serial_connection.in_waiting)
                        buffer += data
                        if b'\n' in buffer:
                            lines = buffer.split(b'\n')
                            for line in lines[:-1]:
                                try:
                                    self.data_received.emit(line.decode('utf-8').strip())
                                except UnicodeDecodeError:
                                    self.data_received.emit(line.decode('latin1', errors='ignore').strip())
                            buffer = lines[-1]
                    except Exception as e:
                        self.data_received.emit(f"Error while reading: {str(e)}")
        except serial.SerialException as e:
            self.data_received.emit(f"Error: {str(e)}")
        finally:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.close()

    def stop(self):
        self.running = False
        self.wait()

    def write_data(self, data):
        try:
            if self.serial_connection and self.serial_connection.is_open:
                self.serial_connection.write(data.encode('utf-8'))
        except Exception as e:
            self.data_received.emit(f"Error while writing: {str(e)}")

class TerminalWindow2(QDialog):
    def __init__(self, board_name, port, baudrate, parent=None):
        super().__init__(parent)
        self.board_name = board_name
        self.port = port
        self.baudrate = baudrate
        self.setWindowTitle(f"{board_name} Interface")
        self.setGeometry(100, 100, 1800, 900)

        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)
        self.info_label = QLabel(f"Connected to {board_name} on port {port} with baudrate {baudrate}")
        self.layout.addWidget(self.info_label)

        self.terminal_output = QPlainTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setWordWrapMode(0)
        font = self.terminal_output.font()
        font.setFamily("Courier")
        font.setPointSize(9)
        self.terminal_output.setFont(font)
        self.terminal_output.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 255, 255);")
        self.layout.addWidget(self.terminal_output)

        self.input_layout = QHBoxLayout()
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Введите команду здесь...")
        self.input_line.returnPressed.connect(self.queue_commands)
        self.input_line.installEventFilter(self)
        self.input_line.setFixedHeight(50)
        self.input_line.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.input_layout.addWidget(self.input_line)

        self.execute_button = QPushButton("Выполнить")
        self.execute_button.clicked.connect(self.queue_commands)
        self.execute_button.setFixedHeight(50)
        self.execute_button.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.execute_button.setFixedWidth(150)
        self.input_layout.addWidget(self.execute_button)

        self.layout.addLayout(self.input_layout)

        self.load_button = QPushButton("Загрузить файл с командами")
        self.load_button.clicked.connect(self.load_commands_from_file)
        self.load_button.setFixedHeight(30)
        self.load_button.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.layout.addWidget(self.load_button)

        self.save_button = QPushButton("Сохранить использованные команды в файл")
        self.save_button.clicked.connect(self.save_commands_to_file)
        self.save_button.setFixedHeight(30)
        self.save_button.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.layout.addWidget(self.save_button)

        self.terminal_log_file = os.path.join(os.getcwd(), "terminal_log.txt")
        with open(self.terminal_log_file, 'w'):  # Перезаписываем файл при открытии
            pass
        self.serial_thread = None
        self.command_queue = []
        self.command_timer = QTimer(self)
        self.command_timer.timeout.connect(self.send_next_command)

        self.commands = []
        self.command_history = []
        self.history_index = -1
        self.suppress_output = True
        self.collecting_commands = False
        self.dicts_results = []
        self.log_file_path = os.path.join(os.getcwd(), "dicts_log.txt")
        self.dicts_command_active = False
        self.start_serial_thread()

        QTimer.singleShot(0, self.input_line.setFocus)

    def start_serial_thread(self):
        self.stop_serial_thread()
        self.serial_thread = SerialThread2(self.port, self.baudrate)
        self.serial_thread.data_received.connect(self.update_terminal)
        self.serial_thread.start()
        self.request_commands()
        self.request_commands2()

    def stop_serial_thread(self):
        if self.serial_thread is not None:
            self.serial_thread.stop()
            self.serial_thread.wait()
            self.serial_thread = None

    def write_dicts_to_file(self):
        try:
            with open(self.log_file_path, 'w', encoding='utf-8') as file:
                for line in self.dicts_results:
                    formatted_line = self.insert_newlines_before_numbers(line)
                    non_empty_lines = [l for l in formatted_line.split('\n') if l.strip()]
                    for non_empty_line in non_empty_lines:
                        file.write(non_empty_line + '\n')
            self.compare_and_write_matches()
        except Exception as e:
            self.update_terminal(f"Error writing to log file: {str(e)}")

    def insert_newlines_before_numbers(self, text):
        return re.sub(r'(\(\d+\))', r'\n\1', text)

    def compare_and_write_matches(self):
        """Сравнивает данные из *_dicts.txt и *_sets.txt и записывает совпадения в log-файл."""
        dict_files = {
            'di_sid_dicts.txt': 'di_sid.txt',
            'di_mid_dicts.txt': 'di_mid.txt',
            'ai_sid_dicts.txt': 'ai_sid.txt',
            'ai_mid_dicts.txt': 'ai_mid.txt'
        }

        with open(self.log_file_path, 'w', encoding='utf-8') as log_file:
            for dict_file, set_file in dict_files.items():
                dict_path = resource_path(dict_file)
                set_path = resource_path(set_file)

                if not os.path.exists(dict_path) or not os.path.exists(set_path):
                    log_file.write(f"Файл {dict_file} или {set_file} не найден.\n")
                    continue

                with open(dict_path, 'r', encoding='utf-8') as file1, \
                     open(set_path, 'r', encoding='utf-8') as file2:
                    dict_lines = [line.strip() for line in file1.readlines()]
                    set_lines = [line.strip() for line in file2.readlines()]

                matches = set(dict_lines) & set(set_lines)
                log_file.write(f"\n[{dict_file}] Совпадения: {len(matches)}\n")
                for match in matches:
                    log_file.write(f"  • {match}\n")




        with open(self.log_file_path, 'r', encoding='utf-8') as log_file:
            print(log_file.read())

    def request_commands(self):
        try:
            self.serial_thread.data_received.connect(self.extract_commands)
            QTimer.singleShot(100, self.send_help_command)
        except Exception as e:
            self.update_terminal(f"Error in request_commands: {str(e)}")

    def send_help_command(self):
        self.serial_thread.write_data('help\r\n')
        QTimer.singleShot(500, self.enable_output)

    def request_commands2(self):
        try:
            self.serial_thread.data_received.connect(self.extract_commands)
            QTimer.singleShot(700, self.send_dicts_command)
        except Exception as e:
            self.update_terminal(f"Error in request_commands: {str(e)}")

    def send_dicts_command(self):
        self.dicts_command_active = True
        self.serial_thread.write_data('dicts\r\n')
        QTimer.singleShot(1000, self.enable_output2)

    def enable_output2(self):
        try:
            self.suppress_output = False
            self.update_terminal("Словарь загружен.\n")
            self.dicts_command_active = False
        except Exception as e:
            self.update_terminal(f"Error in enable_output: {str(e)}")

    def save_results_to_file(self):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить результаты в файл", "",
                                                       "Text Files (*.txt);;All Files (*)", options=options)
            if file_path:
                with open(file_path, 'w') as file:
                    for line in self.dicts_results:
                        file.write(line + '\n')
                self.update_terminal(f"Results successfully saved to {file_path}")
        except Exception as e:
            self.update_terminal(f"Error saving results to file: {str(e)}")

    def enable_output(self):
        try:
            self.suppress_output = False
            self.update_terminal("Команды загружены и готовы к использованию.\n")
        except Exception as e:
            self.update_terminal(f"Error in enable_output: {str(e)}")

    def extract_commands(self, data):
        try:
            lines = data.split('\n')
            for line in lines:
                if 'Available commands:' in line or 'Availible commands:' in line:
                    self.collecting_commands = True
                elif self.collecting_commands:
                    if line.strip() == "":
                        self.collecting_commands = False
                    else:
                        command = line.strip().split()[0]
                        self.commands.append(command)

            if not self.collecting_commands and self.commands:
                self.commands = list(set(self.commands))
                self.serial_thread.data_received.disconnect(self.extract_commands)
        except Exception as e:
            self.update_terminal(f"Error in extract_commands: {str(e)}")

    def format_terminal_output(self, data):
        rows = [line.split() for line in data.split('\n') if line]
        return tabulate(rows, tablefmt="plain")

    def remove_control_chars(self, data):
        ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~]|[\x00-\x1F\x7F])')
        return ansi_escape.sub('', data)

    def update_terminal(self, data):
        try:
            if not self.suppress_output:
                cleaned_data = self.remove_control_chars(data)
                formatted_data = self.format_terminal_output(cleaned_data)
                self.terminal_output.appendPlainText(formatted_data)
                self.log_terminal_output(data)
                if self.dicts_command_active:
                    self.dicts_results.append(cleaned_data)
                    self.write_dicts_to_file()
            self.input_line.setFocus()
        except Exception as e:
            print(f"Error in update_terminal: {str(e)}")

    def log_terminal_output(self, data):
        try:
            with open(self.terminal_log_file, 'a') as file:
                file.write(data + '\n')
        except Exception as e:
            print(f"Error in log_terminal_output: {str(e)}")

    def queue_commands(self):
        try:
            command = self.input_line.text().strip()
            if command:
                self.command_history.append(command)
                self.history_index = len(self.command_history)

            commands = self.input_line.text().split('\n')
            self.input_line.clear()
            self.command_queue.extend(commands)
            if not self.command_timer.isActive():
                self.command_timer.start(100)
        except Exception as e:
            self.update_terminal(f"Error in queue_commands: {str(e)}")

    def send_next_command(self):
        try:
            if self.command_queue:
                next_command = self.command_queue.pop(0)
                self.serial_thread.write_data(next_command + '\r\n')
                self.log_terminal_output(f"$> {next_command}")
                if next_command.strip().lower() == 'reset':
                    QTimer.singleShot(7000, self.command_timer.start)
                    self.command_timer.stop()
            else:
                self.command_timer.stop()
        except Exception as e:
            self.update_terminal(f"Error in send_next_command: {str(e)}")

    def send_data(self):
        try:
            data = self.input_line.text()
            self.input_line.clear()
            self.serial_thread.write_data(data + '\r\n')
        except Exception as e:
            self.update_terminal(f"Error in send_data: {str(e)}")

    def load_commands_from_file(self):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл с командами", "",
                                                       "Text Files (*.txt);;All Files (*)", options=options)
            if file_path:
                self.load_commands(file_path)
                self.input_line.setFocus()
        except Exception as e:
            self.update_terminal(f"Error in load_commands_from_file: {str(e)}")
            self.input_line.setFocus()

    def load_commands(self, file_path):
        try:
            with open(file_path, 'r') as file:
                commands = file.readlines()
                commands = [command.strip() for command in commands if command.strip()]
                self.command_queue.extend(commands)
                if not self.command_timer.isActive():
                    self.command_timer.start(1000)
        except Exception as e:
            self.update_terminal(f"Error in load_commands: {str(e)}")

    def save_commands_to_file(self):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить команды в файл", "",
                                                       "Text Files (*.txt);;All Files (*)", options=options)
            if file_path:
                with open(file_path, 'w') as file:
                    with open(self.terminal_log_file, 'r') as log_file:
                        lines = log_file.readlines()
                        for line in lines:
                            if line.startswith("$>"):
                                file.write(line[2:])
                self.update_terminal(f"Команды успешно сохранены в {file_path}")
        except Exception as e:
            self.update_terminal(f"Error saving commands to file: {str(e)}")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.input_line.setFocus()

    def dropEvent(self, event: QDropEvent):
        try:
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.load_commands(file_path)
                self.input_line.setFocus()
        except Exception as e:
            self.update_terminal(f"Error in dropEvent: {str(e)}")

    def eventFilter(self, source, event):
        try:
            if event.type() == QKeyEvent.KeyPress:
                if event.key() == Qt.Key_Tab:
                    current_text = self.input_line.text()
                    if current_text:
                        matching_commands = [cmd for cmd in self.commands if cmd.startswith(current_text)]
                        if matching_commands:
                            self.input_line.setText(matching_commands[0])
                    return True
                elif event.key() == Qt.Key_Up:
                    if self.history_index > 0:
                        self.history_index -= 1
                        self.input_line.setText(self.command_history[self.history_index])
                    return True
                elif event.key() == Qt.Key_Down:
                    if self.history_index < len(self.command_history) - 1:
                        self.history_index += 1
                        self.input_line.setText(self.command_history[self.history_index])
                    else:
                        self.history_index = len(self.command_history)
                        self.input_line.clear()
                    return True
                elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                    self.queue_commands()
                    return True
            return super(TerminalWindow2, self).eventFilter(source, event)
        except Exception as e:
            self.update_terminal(f"Error in eventFilter: {str(e)}")
            return False

    def send_data(self, data):
        self.serial_thread.write_data(data + '\r\n')

    def closeEvent(self, event):
        try:
            self.stop_serial_thread()
            event.accept()
        except Exception as e:
            self.update_terminal(f"Error in closeEvent: {str(e)}")
