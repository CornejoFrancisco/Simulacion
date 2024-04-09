import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow
from interfaz.selector_parametros import *

class selector_parametros(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialogo()
        self.ui.setupUi(self)
        self.hide_params_norm()
        self.hide_params_expo()
        self.hide_params_unif()
        self.hide_cantIntervalos()
        self.hide_btn_generar()

        self.ui.rd_btn_distr_unif.toggled.connect(self.show_params_unif)
        self.ui.rd_btn_distr_expo.toggled.connect(self.show_params_expo)
        self.ui.rd_btn_distr_norm.toggled.connect(self.show_params_norm)

    def show_params_unif(self):
        for i in range(self.ui.grid_params_uniforme.count()):
            widget = self.ui.grid_params_uniforme.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
        self.hide_params_expo()
        self.hide_params_norm()
        self.show_cantIntervalos()
        self.show_btn_generar()

    def show_params_expo(self):
        for i in range(self.ui.grid_params_exponencial.count()):
            widget = self.ui.grid_params_exponencial.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
        self.hide_params_unif()
        self.hide_params_norm()
        self.hide_cantIntervalos()
        self.show_cantIntervalos()
        self.show_btn_generar()

    def show_params_norm(self):
        for i in range(self.ui.grid_params_normal.count()):
            widget = self.ui.grid_params_normal.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
        self.hide_params_unif()
        self.hide_params_expo()
        self.show_cantIntervalos()
        self.show_btn_generar()

    def show_cantIntervalos(self):
        for i in range(self.ui.lyt_h_lbl_cant_intervalos.count()):
            widget = self.ui.lyt_h_lbl_cant_intervalos.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
        for i in range(self.ui.lyt_h_rd_btn_cant_intervalos.count()):
            widget = self.ui.lyt_h_rd_btn_cant_intervalos.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
    def show_btn_generar(self):
        self.ui.btn_generar.setHidden(False)

    def hide_params_norm(self):
        for i in range(self.ui.grid_params_normal.count()):
            widget = self.ui.grid_params_normal.itemAt(i).widget()
            if widget:
                widget.setHidden(True)

    def hide_params_expo(self):
        for i in range(self.ui.grid_params_exponencial.count()):
            widget = self.ui.grid_params_exponencial.itemAt(i).widget()
            if widget:
                widget.setHidden(True)

    def hide_params_unif(self):
        for i in range(self.ui.grid_params_uniforme.count()):
            widget = self.ui.grid_params_uniforme.itemAt(i).widget()
            if widget:
                widget.setHidden(True)
    def hide_cantIntervalos(self):
        for i in range(self.ui.lyt_h_lbl_cant_intervalos.count()):
            widget = self.ui.lyt_h_lbl_cant_intervalos.itemAt(i).widget()
            if widget:
                widget.setHidden(True)
        for i in range(self.ui.lyt_h_rd_btn_cant_intervalos.count()):
            widget = self.ui.lyt_h_rd_btn_cant_intervalos.itemAt(i).widget()
            if widget:
                widget.setHidden(True)
    def hide_btn_generar(self):
        self.ui.btn_generar.setHidden(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = selector_parametros()
    ventana.show()
    sys.exit(app.exec())
