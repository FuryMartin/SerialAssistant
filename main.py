from distutils.util import change_root
from qt_core import *
from ui_window import Ui_MainWindow
import sys
import serial
import serial.tools.list_ports
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SerialAssistant")
        self.show()

        #设置按钮互斥
        self.mode_group = QButtonGroup(self)
        self.mode_group.addButton(self.ui.FSK_mode)
        self.mode_group.addButton(self.ui.Lora_mode)
        self.mode_group.setExclusive(True)

        #设置槽函数
        self.ui.Confirm_button.clicked.connect(self.button_click)

        #设置串口
        self.ser = serial.Serial()
        self.port_check()
        self.ui.port_selector.currentTextChanged.connect(self.change_port)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.receive_data)

        self.received_data = ''

    def port_check(self):
        self.com_dictionary = {}
        port_list = list(serial.tools.list_ports.comports())
        for port in port_list:
            self.com_dictionary["%s" % port[0]] = "%s" % port[1]
            #self.ui.IO_window.append(port[0])
            self.ui.port_selector.addItem(port[0])
    
    def change_port(self):
        self.selected_port = self.ui.port_selector.currentText()
        self.open_port()

    def open_port(self):
        self.ser.port = self.selected_port
        self.ser.baudrate = 9600

        try:
            self.ser.open()
            print("port open")
        except:
            QMessageBox.critical(self,"Port Error", "此串口不能被打开！")
            return None

        self.timer.start(2)

    def close_port(self):
        self.timer.stop()
        try:
            self.ser.close()
        except:
            pass
    
    def send_data(self):
        if self.ser.isOpen():
            num = self.ser.write(self.arguments.encode('utf-8'))
            #print(num)
        else:
            pass
    
    def receive_data(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None 
        if num > 0:
            data = self.ser.read(num)
            num = len(data)
            if data.decode('utf-8') != '':
            #self.received_data += data.decode('utf-8')
                self.ui.IO_window.append(data.decode('utf-8'))
            
            text_cursor =self.ui.IO_window.textCursor()
            text_cursor.movePosition(text_cursor.End)
            self.ui.IO_window.setTextCursor(text_cursor)
        else:
            #self.received_data = ''
            pass

    def button_click(self):
        checked_item = self.mode_group.checkedButton()
        #print(checked_item.objectName())
        if checked_item.objectName() == "FSK_mode":
            #self.ui.IO_window.append("选中模式：\tFSK")
            FSK_frequency = self.ui.FSK_frequency.currentText().split(" ")[0]
            FSK_power = self.ui.FSK_power.currentText()
            FSK_bitrate = self.ui.FSK_bitrate.currentText()
            FSK_bandwidth = self.ui.FSK_bandwidth.currentText().split(" ")[0]
            self.arguments = "发送参数：\t0;{};{};{};{}".format(FSK_frequency,FSK_power,FSK_bitrate,FSK_bandwidth)
            #self.arguments = '1'
            self.send_data()
        else:
            #self.ui.IO_window.append("选中模式：\tLora")
            Lora_frequency = self.ui.Lora_frequency.currentText().split(" ")[0]
            Lora_power = self.ui.Lora_power.currentText()
            Lora_spreadingfactor = self.ui.Lora_spreadingfactor.currentText()
            Lora_bandwidth = self.ui.Lora_bandwidth.currentText().split(" ")[0]
            self.arguments = "发送参数：\t1;{};{};{};{}".format(Lora_frequency,Lora_power,Lora_bandwidth,Lora_spreadingfactor)
            #self.arguments = '2'
            self.send_data()
        self.ui.IO_window.append(self.arguments)
        #print()

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    icon_path = os.path.join(current_dir, 'icon.ico')
    app.setWindowIcon(QIcon(icon_path))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
        