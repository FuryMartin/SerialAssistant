from qt_core import *
from ui_window import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.mode_group = QButtonGroup(self)
        self.mode_group.addButton(self.ui.FSK_mode)
        self.mode_group.addButton(self.ui.Lora_mode)
        self.mode_group.setExclusive(True)

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
        