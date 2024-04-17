import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QDoubleSpinBox, QSpinBox, QRadioButton
from interfaz.selector_parametros import *
from scripts.main import *


class selector_parametros(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Dialogo()
        self.ui.setupUi(self)

        self.cantidad_nros = 0
        self.valor_a = 0
        self.valor_b = 0
        self.cantidad_intervalos = 0
        self.opcion_dist_expo = 0
        self.valor_op_dist_expo = 0
        self.media = 0
        self.desviacion = 0

        self.hide_params_norm()
        self.hide_params_expo()
        self.hide_params_unif()
        self.hide_cantIntervalos()
        self.hide_btn_generar()

        self.ui.rd_btn_distr_unif.toggled.connect(self.dist_unif)
        self.ui.rd_btn_distr_expo.toggled.connect(self.dist_expo)
        self.ui.rd_btn_distr_norm.toggled.connect(self.dist_norm)

        self.ui.btn_generar.clicked.connect(self.send_data)

    def show_alert(self, mensaje):
        alert = QMessageBox()
        alert.setText(mensaje)
        alert.exec()

    def dist_unif(self):
        self.clear_parametros()
        self.show_params_unif()

        self.ui.spn_box_cant_nros_unif.valueChanged.connect(self.set_cant_nros)
        self.ui.spn_box_a_unif.valueChanged.connect(self.set_valor_a)
        self.ui.spn_box_b_unif.valueChanged.connect(self.set_valor_b)

        self.extract_cant_intervalos()

    def dist_expo(self):
        self.clear_parametros()
        self.show_params_expo()
        self.ui.spn_box_cant_nros_expo.valueChanged.connect(self.set_cant_nros)

        self.ui.rd_btn_lambda_expo.toggled.connect(lambda: self.set_opt_expo(value=1))
        self.ui.rd_btn_media_expo.toggled.connect(lambda: self.set_opt_expo(value=2))

        self.ui.spn_box_media_lambda_expo.valueChanged.connect(self.set_value_opt_expo)

        self.extract_cant_intervalos()

    def set_value_opt_expo(self, value):
        self.valor_op_dist_expo = value

    def set_opt_expo(self, value):
        self.opcion_dist_expo = value

    def dist_norm(self):
        self.clear_parametros()
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
        self.media = value

    def set_value_desviacion(self, value):
        self.desviacion = value

    def validar_datos_comunes(self):
        datos_comunes_ok = True
        if self.cantidad_nros == 0:
            datos_comunes_ok = False
            self.show_alert("Error , Debe ingresar una cantidad de numeros a generar positiva")
        if self.cantidad_intervalos == 0:
            datos_comunes_ok = False
            self.show_alert("Error , debe seleccionar una cantidad de intervalos")
        return datos_comunes_ok

    def validar_datos_unif(self):
        todo_ok = True
        if self.valor_a >= self.valor_b:
            todo_ok = False
            self.show_alert("Error , el valor de B debe ser mayor A")
        return todo_ok

    def validar_datos_expo(self):
        todo_ok = True
        if self.opcion_dist_expo == 0:
            todo_ok = False
            self.show_alert("Error , debe seleccionar si usar lambda o la media")
        if self.valor_op_dist_expo <= 0 and self.opcion_dist_expo == 1:
            todo_ok = False
            self.show_alert("Error , el valor de lambda debe ser mayor a cero")
        if self.valor_op_dist_expo <= 0 and self.opcion_dist_expo == 2:
            todo_ok = False
            self.show_alert("Error , el valor de la media debe ser mayor a cero")
        return todo_ok

    def send_data(self):
        print(self.cantidad_intervalos)
        if self.validar_datos_comunes():
            if self.ui.rd_btn_distr_norm.isChecked():
                params_norm = {"cantidad_nros": self.cantidad_nros , "media": self.media,
                               "desviacion": self.desviacion, "cantidad_intervalos": self.cantidad_intervalos}
                print("PARAMETROS NORMAL: ", params_norm)
                generar_distribucion_normal(params_norm)

            elif self.ui.rd_btn_distr_unif.isChecked():
                if self.validar_datos_unif():
                    params_unif = {"cantidad_nros": self.cantidad_nros, "valor_a": self.valor_a,
                                   "valor_b": self.valor_b, "cantidad_intervalos": self.cantidad_intervalos}
                    print("PARAMETROS UNIFORME: ", params_unif)
                    generar_distribucion_uniforme(params_unif)

            elif self.ui.rd_btn_distr_expo.isChecked():
                if self.validar_datos_expo():
                    params_expo = {"cantidad_nros": self.cantidad_nros, "opcion_dist": self.opcion_dist_expo,
                                   "valor_op_dist": self.valor_op_dist_expo,
                                   "cantidad_intervalos": self.cantidad_intervalos}
                    print("PARAMETROS_EXPONENCIAL: ", params_expo)
                    generar_distribucion_exponencial(params_expo)

    def set_cant_intervals(self, value):
        self.cantidad_intervalos = value

    def set_cant_nros(self, value):
        self.cantidad_nros = value

    def set_valor_a(self, value):
        self.valor_a = value

    def set_valor_b(self, value):
        self.valor_b = value

    def clear_parametros(self):
        self.cantidad_nros = 0
        self.valor_a = 0
        self.valor_b = 0
        self.opcion_dist_expo = 0
        self.media = 0
        self.desviacion = 0

    def show_params_unif(self):
        for i in range(self.ui.grid_params_uniforme.count()):
            widget = self.ui.grid_params_uniforme.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
                if isinstance(widget, QDoubleSpinBox) or isinstance(widget, QSpinBox):
                    widget.setValue(0)
        self.hide_params_expo()
        self.hide_params_norm()
        self.show_cantIntervalos()
        self.show_btn_generar()

    def show_params_expo(self):

        for i in range(self.ui.grid_params_exponencial.count()):
            widget = self.ui.grid_params_exponencial.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
                if isinstance(widget, QDoubleSpinBox) or isinstance(widget, QSpinBox):
                    widget.setValue(0)
        self.hide_params_unif()
        self.hide_params_norm()
        self.show_cantIntervalos()
        self.show_btn_generar()

    def show_params_norm(self):
        for i in range(self.ui.grid_params_normal.count()):
            widget = self.ui.grid_params_normal.itemAt(i).widget()
            if widget:
                widget.setHidden(False)
                if isinstance(widget, QDoubleSpinBox) or isinstance(widget, QSpinBox):
                    widget.setValue(0)
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
