from qt_core import *
from ui_window import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


        #设置按钮互斥
        self.mode_group = QButtonGroup(self)
        self.mode_group.addButton(self.ui.FSK_mode)
        self.mode_group.addButton(self.ui.Lora_mode)
        self.mode_group.setExclusive(True)

        #设置槽函数
        self.ui.Confirm_button.clicked.connect(self.button_click)

    def button_click(self):
        checked_item = self.mode_group.checkedButton()
        print(checked_item.objectName())
        if checked_item.objectName() == "FSK_mode":
            self.ui.IO_window.append("选中模式：\tFSK")
            FSK_frequency = self.ui.FSK_frequency.currentText().split(" ")[0]
            FSK_power = self.ui.FSK_power.currentText()
            FSK_bitrate = self.ui.FSK_bitrate.currentText()
            FSK_bandwidth = self.ui.FSK_bandwidth.currentText().split(" ")[0]
            self.arguments = "发送参数：\t0;{};{};{};{}".format(FSK_frequency,FSK_power,FSK_bitrate,FSK_bandwidth)
            self.ui.IO_window.append(self.arguments)
        else:
            self.ui.IO_window.append("选中模式：\tLora")
            Lora_frequency = self.ui.Lora_frequency.currentText().split(" ")[0]
            Lora_power = self.ui.Lora_power.currentText()
            Lora_spreadingfactor = self.ui.Lora_spreadingfactor.currentText()
            Lora_bandwidth = self.ui.Lora_bandwidth.currentText().split(" ")[0]
            self.arguments = "发送参数：\t1;{};{};{};{}".format(Lora_frequency,Lora_power,Lora_bandwidth,Lora_spreadingfactor)
            self.ui.IO_window.append(self.arguments)
        #print()

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
        