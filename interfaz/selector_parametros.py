# Form implementation generated from reading ui file '.\selector_parametros.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Dialogo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(941, 586)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 520, 821, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.layout_v_btn_generar = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_v_btn_generar.setContentsMargins(0, 0, 0, 0)
        self.layout_v_btn_generar.setObjectName("layout_v_btn_generar")
        self.btn_generar = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        self.btn_generar.setObjectName("btn_generar")
        self.layout_v_btn_generar.addWidget(self.btn_generar)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 129, 945, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_params = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_params.setContentsMargins(0, 0, 0, 0)
        self.grid_params.setObjectName("grid_params")
        self.grid_params_exponencial = QtWidgets.QGridLayout()
        self.grid_params_exponencial.setObjectName("grid_params_exponencial")
        self.spn_box_cant_nros_expo = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_cant_nros_expo.setMaximum(1000000)
        self.spn_box_cant_nros_expo.setObjectName("spn_box_cant_nros_expo")
        self.grid_params_exponencial.addWidget(self.spn_box_cant_nros_expo, 2, 0, 1, 1)
        self.lbl_media_lambda_expo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_media_lambda_expo.setObjectName("lbl_media_lambda_expo")
        self.grid_params_exponencial.addWidget(self.lbl_media_lambda_expo, 6, 0, 1, 1)
        self.rd_btn_lambda_expo = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rd_btn_lambda_expo.setObjectName("rd_btn_lambda_expo")
        self.grid_params_exponencial.addWidget(self.rd_btn_lambda_expo, 4, 0, 1, 1)
        self.lbl_params_expo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_params_expo.setObjectName("lbl_params_expo")
        self.grid_params_exponencial.addWidget(self.lbl_params_expo, 0, 0, 1, 1)
        self.rd_btn_media_expo = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.rd_btn_media_expo.setObjectName("rd_btn_media_expo")
        self.grid_params_exponencial.addWidget(self.rd_btn_media_expo, 5, 0, 1, 1)
        self.lbl_cant_nrs_expo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_cant_nrs_expo.setObjectName("lbl_cant_nrs_expo")
        self.grid_params_exponencial.addWidget(self.lbl_cant_nrs_expo, 1, 0, 1, 1)
        self.lbl_selec_media_lambda_expo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_selec_media_lambda_expo.setObjectName("lbl_selec_media_lambda_expo")
        self.grid_params_exponencial.addWidget(self.lbl_selec_media_lambda_expo, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.grid_params_exponencial.addItem(spacerItem, 8, 0, 1, 1)
        self.spn_box_media_lambda_expo = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_media_lambda_expo.setDecimals(4)
        self.spn_box_media_lambda_expo.setMinimum(-1e+85)
        self.spn_box_media_lambda_expo.setMaximum(1e+144)
        self.spn_box_media_lambda_expo.setObjectName("spn_box_media_lambda_expo")
        self.grid_params_exponencial.addWidget(self.spn_box_media_lambda_expo, 7, 0, 1, 1)
        self.grid_params.addLayout(self.grid_params_exponencial, 0, 1, 1, 1)
        self.grid_params_uniforme = QtWidgets.QGridLayout()
        self.grid_params_uniforme.setObjectName("grid_params_uniforme")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.grid_params_uniforme.addItem(spacerItem1, 12, 0, 1, 1)
        self.lbl_cant_nros_unif = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_cant_nros_unif.setObjectName("lbl_cant_nros_unif")
        self.grid_params_uniforme.addWidget(self.lbl_cant_nros_unif, 3, 0, 1, 1)
        self.lbl_parma_unif = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_parma_unif.setObjectName("lbl_parma_unif")
        self.grid_params_uniforme.addWidget(self.lbl_parma_unif, 0, 0, 1, 1)
        self.lbl_b_unif = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_b_unif.setObjectName("lbl_b_unif")
        self.grid_params_uniforme.addWidget(self.lbl_b_unif, 10, 0, 1, 1)
        self.lbl_a_unif = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_a_unif.setObjectName("lbl_a_unif")
        self.grid_params_uniforme.addWidget(self.lbl_a_unif, 5, 0, 1, 1)
        self.spn_box_cant_nros_unif = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_cant_nros_unif.setMaximum(1000000)
        self.spn_box_cant_nros_unif.setObjectName("spn_box_cant_nros_unif")
        self.grid_params_uniforme.addWidget(self.spn_box_cant_nros_unif, 4, 0, 1, 1)
        self.spn_box_a_unif = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_a_unif.setDecimals(4)
        self.spn_box_a_unif.setMinimum(-1e+106)
        self.spn_box_a_unif.setMaximum(1e+112)
        self.spn_box_a_unif.setProperty("value", 0.0)
        self.spn_box_a_unif.setObjectName("spn_box_a_unif")
        self.grid_params_uniforme.addWidget(self.spn_box_a_unif, 6, 0, 1, 1)
        self.spn_box_b_unif = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_b_unif.setKeyboardTracking(True)
        self.spn_box_b_unif.setDecimals(4)
        self.spn_box_b_unif.setMinimum(-1e+40)
        self.spn_box_b_unif.setMaximum(1e+60)
        self.spn_box_b_unif.setObjectName("spn_box_b_unif")
        self.grid_params_uniforme.addWidget(self.spn_box_b_unif, 11, 0, 1, 1)
        self.grid_params.addLayout(self.grid_params_uniforme, 0, 0, 1, 1)
        self.grid_params_normal = QtWidgets.QGridLayout()
        self.grid_params_normal.setObjectName("grid_params_normal")
        self.spn_box_cant_nros_norm = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_cant_nros_norm.setMaximum(1000000)
        self.spn_box_cant_nros_norm.setObjectName("spn_box_cant_nros_norm")
        self.grid_params_normal.addWidget(self.spn_box_cant_nros_norm, 2, 0, 1, 1)
        self.lbl_cant_nros_norm = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_cant_nros_norm.setObjectName("lbl_cant_nros_norm")
        self.grid_params_normal.addWidget(self.lbl_cant_nros_norm, 1, 0, 1, 1)
        self.lbl_desv_norm = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_desv_norm.setObjectName("lbl_desv_norm")
        self.grid_params_normal.addWidget(self.lbl_desv_norm, 5, 0, 1, 1)
        self.lbl_media_norm = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_media_norm.setObjectName("lbl_media_norm")
        self.grid_params_normal.addWidget(self.lbl_media_norm, 3, 0, 1, 1)
        self.lbl_params_norm = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.lbl_params_norm.setObjectName("lbl_params_norm")
        self.grid_params_normal.addWidget(self.lbl_params_norm, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.grid_params_normal.addItem(spacerItem2, 7, 0, 1, 1)
        self.spn_box_media_norm = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_media_norm.setDecimals(4)
        self.spn_box_media_norm.setMaximum(1e+76)
        self.spn_box_media_norm.setObjectName("spn_box_media_norm")
        self.grid_params_normal.addWidget(self.spn_box_media_norm, 4, 0, 1, 1)
        self.spn_box_desv_norm = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spn_box_desv_norm.setDecimals(4)
        self.spn_box_desv_norm.setObjectName("spn_box_desv_norm")
        self.grid_params_normal.addWidget(self.spn_box_desv_norm, 6, 0, 1, 1)
        self.grid_params.addLayout(self.grid_params_normal, 0, 2, 1, 1)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(19, 439, 821, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layout_v_cant_intervalos = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_v_cant_intervalos.setContentsMargins(0, 0, 0, 0)
        self.layout_v_cant_intervalos.setObjectName("layout_v_cant_intervalos")
        self.lyt_h_lbl_cant_intervalos = QtWidgets.QHBoxLayout()
        self.lyt_h_lbl_cant_intervalos.setObjectName("lyt_h_lbl_cant_intervalos")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_lbl_cant_intervalos.addItem(spacerItem3)
        self.lbl_cantidad_intervalos = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.lbl_cantidad_intervalos.setObjectName("lbl_cantidad_intervalos")
        self.lyt_h_lbl_cant_intervalos.addWidget(self.lbl_cantidad_intervalos)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_lbl_cant_intervalos.addItem(spacerItem4)
        self.layout_v_cant_intervalos.addLayout(self.lyt_h_lbl_cant_intervalos)
        self.lyt_h_rd_btn_cant_intervalos = QtWidgets.QHBoxLayout()
        self.lyt_h_rd_btn_cant_intervalos.setObjectName("lyt_h_rd_btn_cant_intervalos")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_rd_btn_cant_intervalos.addItem(spacerItem5)
        self.rd_btn_10 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4)
        self.rd_btn_10.setObjectName("rd_btn_10")
        self.lyt_h_rd_btn_cant_intervalos.addWidget(self.rd_btn_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_rd_btn_cant_intervalos.addItem(spacerItem6)
        self.rd_btn_15 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4)
        self.rd_btn_15.setObjectName("rd_btn_15")
        self.lyt_h_rd_btn_cant_intervalos.addWidget(self.rd_btn_15)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_rd_btn_cant_intervalos.addItem(spacerItem7)
        self.rd_btn_20 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4)
        self.rd_btn_20.setObjectName("rd_btn_20")
        self.lyt_h_rd_btn_cant_intervalos.addWidget(self.rd_btn_20)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_rd_btn_cant_intervalos.addItem(spacerItem8)
        self.rd_btn_25 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_4)
        self.rd_btn_25.setObjectName("rd_btn_25")
        self.lyt_h_rd_btn_cant_intervalos.addWidget(self.rd_btn_25)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_rd_btn_cant_intervalos.addItem(spacerItem9)
        self.layout_v_cant_intervalos.addLayout(self.lyt_h_rd_btn_cant_intervalos)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 821, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_v_titulo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_v_titulo.setContentsMargins(0, 0, 0, 0)
        self.layout_v_titulo.setObjectName("layout_v_titulo")
        self.layout_h_titulo = QtWidgets.QHBoxLayout()
        self.layout_h_titulo.setObjectName("layout_h_titulo")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layout_h_titulo.addItem(spacerItem10)
        self.label_titulo = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_titulo.setObjectName("label_titulo")
        self.layout_h_titulo.addWidget(self.label_titulo)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.layout_h_titulo.addItem(spacerItem11)
        self.layout_v_titulo.addLayout(self.layout_h_titulo)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 821, 52))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_v_tipo_distribucion = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_v_tipo_distribucion.setContentsMargins(0, 0, 0, 0)
        self.layout_v_tipo_distribucion.setObjectName("layout_v_tipo_distribucion")
        self.lyt_h_select_distr = QtWidgets.QHBoxLayout()
        self.lyt_h_select_distr.setObjectName("lyt_h_select_distr")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_select_distr.addItem(spacerItem12)
        self.lbl_titulo_select_distr = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.lbl_titulo_select_distr.setObjectName("lbl_titulo_select_distr")
        self.lyt_h_select_distr.addWidget(self.lbl_titulo_select_distr)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.lyt_h_select_distr.addItem(spacerItem13)
        self.layout_v_tipo_distribucion.addLayout(self.lyt_h_select_distr)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.rd_btn_distr_unif = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.rd_btn_distr_unif.setObjectName("rd_btn_distr_unif")
        self.horizontalLayout_4.addWidget(self.rd_btn_distr_unif)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.rd_btn_distr_expo = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.rd_btn_distr_expo.setObjectName("rd_btn_distr_expo")
        self.horizontalLayout_4.addWidget(self.rd_btn_distr_expo)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.rd_btn_distr_norm = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.rd_btn_distr_norm.setObjectName("rd_btn_distr_norm")
        self.horizontalLayout_4.addWidget(self.rd_btn_distr_norm)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.layout_v_tipo_distribucion.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_generar.setText(_translate("Dialog", "Generar distribucion"))
        self.lbl_media_lambda_expo.setText(_translate("Dialog", "Ingrese el valor:"))
        self.rd_btn_lambda_expo.setText(_translate("Dialog", "Lambda"))
        self.lbl_params_expo.setText(_translate("Dialog", "Parametros exponencial"))
        self.rd_btn_media_expo.setText(_translate("Dialog", "Media"))
        self.lbl_cant_nrs_expo.setText(_translate("Dialog", "Cantidad de numeros a generar:"))
        self.lbl_selec_media_lambda_expo.setText(_translate("Dialog", "Seleccione:"))
        self.lbl_cant_nros_unif.setText(_translate("Dialog", "Cantidad de numeros a generar:"))
        self.lbl_parma_unif.setText(_translate("Dialog", "Parametros uniforme"))
        self.lbl_b_unif.setText(_translate("Dialog", "B:"))
        self.lbl_a_unif.setText(_translate("Dialog", "A:"))
        self.lbl_cant_nros_norm.setText(_translate("Dialog", "Cantidad de numeros a generar:"))
        self.lbl_desv_norm.setText(_translate("Dialog", "Desviacion"))
        self.lbl_media_norm.setText(_translate("Dialog", "Media:"))
        self.lbl_params_norm.setText(_translate("Dialog", "Parametros normal"))
        self.lbl_cantidad_intervalos.setText(_translate("Dialog", "Cantidad de intervalos"))
        self.rd_btn_10.setText(_translate("Dialog", "10"))
        self.rd_btn_15.setText(_translate("Dialog", "15"))
        self.rd_btn_20.setText(_translate("Dialog", "20"))
        self.rd_btn_25.setText(_translate("Dialog", "25"))
        self.label_titulo.setText(_translate("Dialog", "TP2 - SIMULACION"))
        self.lbl_titulo_select_distr.setText(_translate("Dialog", "SELECCIONE EL TIPO DE DISTRIBUCION"))
        self.rd_btn_distr_unif.setText(_translate("Dialog", "Uniforme"))
        self.rd_btn_distr_expo.setText(_translate("Dialog", "Exponencial"))
        self.rd_btn_distr_norm.setText(_translate("Dialog", "Normal"))
