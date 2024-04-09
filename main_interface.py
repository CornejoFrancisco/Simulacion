import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow
from interfaz.selector_parametros import *
from scripts.main import *


class selector_parametros(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialogo()
        self.ui.setupUi(self)

        self.params_unif = {"cantidad_nros": None, "valor_a": None, "valor_b": None, "cantidad_intervalos": None}
        self.params_expo = {"cantidad_nros": None, "opcion_dist": None, "valor_op_dist": None,
                            "cantidad_intervalos": None}
        self.params_norm = {"cantidad_nros": None, "media": None, "desviacion": None, "cantidad_intervalos": None}

        self.hide_params_norm()
        self.hide_params_expo()
        self.hide_params_unif()
        self.hide_cantIntervalos()
        self.hide_btn_generar()

        self.ui.rd_btn_distr_unif.toggled.connect(self.dist_unif)
        self.ui.rd_btn_distr_expo.toggled.connect(self.dist_expo)
        self.ui.rd_btn_distr_norm.toggled.connect(self.dist_norm)

        self.ui.btn_generar.clicked.connect(self.send_data)

    def dist_unif(self):

        self.params_unif.clear()
        self.show_params_unif()

        self.ui.spn_box_cant_nros_unif.valueChanged.connect(self.set_cant_nros)
        self.ui.spn_box_a_unif.valueChanged.connect(self.set_valor_a)
        self.ui.spn_box_b_unif.valueChanged.connect(self.set_valor_b)

        self.extract_cant_intervalos()

    def dist_expo(self):

        self.params_expo.clear()
        self.show_params_expo()
        self.ui.spn_box_cant_nros_expo.valueChanged.connect(self.set_cant_nros)

        self.ui.rd_btn_lambda_expo.toggled.connect(lambda: self.set_opt_expo(value=1))
        self.ui.rd_btn_media_expo.toggled.connect(lambda: self.set_opt_expo(value=2))

        self.ui.spn_box_media_lambda_expo.valueChanged.connect(self.set_value_opt_expo)

        self.extract_cant_intervalos()

    def set_value_opt_expo(self, value):
        self.params_expo["valor_op_dist"] = value

    def set_opt_expo(self, value):
        self.params_expo["opcion_dist"] = value

    def dist_norm(self):

        self.params_norm.clear()
        self.show_params_norm()

        self.ui.spn_box_cant_nros_norm.valueChanged.connect(self.set_cant_nros)

        self.ui.spn_box_media_norm.valueChanged.connect(self.set_value_media)
        self.ui.spn_box_desv_norm.valueChanged.connect(self.set_value_desviacion)

        self.extract_cant_intervalos()

    def extract_cant_intervalos(self):
        self.ui.rd_btn_10.toggled.connect(lambda: self.set_cant_intervals(value=10))
        self.ui.rd_btn_15.toggled.connect(lambda: self.set_cant_intervals(value=15))
        self.ui.rd_btn_20.toggled.connect(lambda: self.set_cant_intervals(value=20))
        self.ui.rd_btn_25.toggled.connect(lambda: self.set_cant_intervals(value=25))

    def set_value_media(self, value):
        self.params_norm["media"] = value

    def set_value_desviacion(self, value):
        self.params_norm["desviacion"] = value

    def send_data(self):

        if self.ui.rd_btn_distr_norm.isChecked():
            print("PARAMETROS NORMAL: ", self.params_norm)
            generar_distribucion_normal(self.params_norm)

        elif self.ui.rd_btn_distr_unif.isChecked():
            print("PARAMETROS UNIFORME: ", self.params_unif)
            generar_distribucion_uniforme(self.params_unif)

        elif self.ui.rd_btn_distr_expo.isChecked():
            print("PARAMETROS_EXPONENCIAL: ", self.params_expo)
            generar_distribucion_exponencial(self.params_expo)

    def set_cant_intervals(self, value):

        if self.ui.rd_btn_distr_norm.isChecked():
            self.params_norm["cantidad_intervalos"] = value

        elif self.ui.rd_btn_distr_unif.isChecked():
            self.params_unif["cantidad_intervalos"] = value

        elif self.ui.rd_btn_distr_expo.isChecked():
            self.params_expo["cantidad_intervalos"] = value

    def set_cant_nros(self, value):

        if self.ui.rd_btn_distr_norm.isChecked():
            self.params_norm["cantidad_nros"] = value

        elif self.ui.rd_btn_distr_unif.isChecked():
            self.params_unif["cantidad_nros"] = value

        elif self.ui.rd_btn_distr_expo.isChecked():
            self.params_expo["cantidad_nros"] = value

    def set_valor_a(self, value):
        self.params_unif["valor_a"] = value

    def set_valor_b(self, value):
        self.params_unif["valor_b"] = value

    def clear_dict(self, dic):

        for clave in dic:
            dic[clave] = None

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
