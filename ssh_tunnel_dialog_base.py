# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ssh_tunnel_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeokodowanieAdresowDialogBase(object):
    def setupUi(self, GeokodowanieAdresowDialogBase):
        GeokodowanieAdresowDialogBase.setObjectName("GeokodowanieAdresowDialogBase")
        GeokodowanieAdresowDialogBase.resize(383, 529)
        self.layoutWidget = QtWidgets.QWidget(GeokodowanieAdresowDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 351, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_server = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_server.setObjectName("lbl_server")
        self.horizontalLayout.addWidget(self.lbl_server)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.led_server = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_server.sizePolicy().hasHeightForWidth())
        self.led_server.setSizePolicy(sizePolicy)
        self.led_server.setMinimumSize(QtCore.QSize(200, 0))
        self.led_server.setMaxLength(255)
        self.led_server.setObjectName("led_server")
        self.horizontalLayout.addWidget(self.led_server)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_sshport = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_sshport.setObjectName("lbl_sshport")
        self.horizontalLayout_2.addWidget(self.lbl_sshport)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.sbx_sshport = QtWidgets.QSpinBox(self.layoutWidget)
        self.sbx_sshport.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sbx_sshport.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sbx_sshport.setKeyboardTracking(False)
        self.sbx_sshport.setMinimum(1)
        self.sbx_sshport.setMaximum(99999)
        self.sbx_sshport.setProperty("value", 22)
        self.sbx_sshport.setObjectName("sbx_sshport")
        self.horizontalLayout_2.addWidget(self.sbx_sshport)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_user = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_user.setObjectName("lbl_user")
        self.horizontalLayout_4.addWidget(self.lbl_user)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.led_user = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_user.sizePolicy().hasHeightForWidth())
        self.led_user.setSizePolicy(sizePolicy)
        self.led_user.setMinimumSize(QtCore.QSize(200, 0))
        self.led_user.setText("")
        self.led_user.setMaxLength(255)
        self.led_user.setObjectName("led_user")
        self.horizontalLayout_4.addWidget(self.led_user)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_pass = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pass.setObjectName("lbl_pass")
        self.horizontalLayout_5.addWidget(self.lbl_pass)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.led_pass = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_pass.sizePolicy().hasHeightForWidth())
        self.led_pass.setSizePolicy(sizePolicy)
        self.led_pass.setMinimumSize(QtCore.QSize(200, 0))
        self.led_pass.setMaxLength(255)
        self.led_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.led_pass.setPlaceholderText("")
        self.led_pass.setObjectName("led_pass")
        self.horizontalLayout_5.addWidget(self.led_pass)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_rport = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_rport.setObjectName("lbl_rport")
        self.horizontalLayout_7.addWidget(self.lbl_rport)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.sbx_rport = QtWidgets.QSpinBox(self.layoutWidget)
        self.sbx_rport.setMinimumSize(QtCore.QSize(0, 0))
        self.sbx_rport.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sbx_rport.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sbx_rport.setKeyboardTracking(True)
        self.sbx_rport.setMinimum(1)
        self.sbx_rport.setMaximum(99999)
        self.sbx_rport.setProperty("value", 5432)
        self.sbx_rport.setObjectName("sbx_rport")
        self.horizontalLayout_7.addWidget(self.sbx_rport)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_lport = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_lport.setObjectName("lbl_lport")
        self.horizontalLayout_3.addWidget(self.lbl_lport)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.sbx_lport = QtWidgets.QSpinBox(self.layoutWidget)
        self.sbx_lport.setMinimumSize(QtCore.QSize(0, 0))
        self.sbx_lport.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sbx_lport.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sbx_lport.setKeyboardTracking(True)
        self.sbx_lport.setMinimum(1)
        self.sbx_lport.setMaximum(99999)
        self.sbx_lport.setProperty("value", 55667)
        self.sbx_lport.setObjectName("sbx_lport")
        self.horizontalLayout_3.addWidget(self.sbx_lport)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lbl_pluginVersion = QtWidgets.QLabel(GeokodowanieAdresowDialogBase)
        self.lbl_pluginVersion.setGeometry(QtCore.QRect(20, 501, 191, 20))
        self.lbl_pluginVersion.setObjectName("lbl_pluginVersion")
        self.lbl_copyrights = QtWidgets.QLabel(GeokodowanieAdresowDialogBase)
        self.lbl_copyrights.setGeometry(QtCore.QRect(210, 500, 191, 21))
        self.lbl_copyrights.setTextFormat(QtCore.Qt.RichText)
        self.lbl_copyrights.setOpenExternalLinks(True)
        self.lbl_copyrights.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lbl_copyrights.setObjectName("lbl_copyrights")
        self.groupBox = QtWidgets.QGroupBox(GeokodowanieAdresowDialogBase)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 351, 111))
        self.groupBox.setObjectName("groupBox")
        self.rbn_pass = QtWidgets.QRadioButton(self.groupBox)
        self.rbn_pass.setGeometry(QtCore.QRect(20, 20, 181, 17))
        self.rbn_pass.setChecked(True)
        self.rbn_pass.setObjectName("rbn_pass")
        self.rbn_key = QtWidgets.QRadioButton(self.groupBox)
        self.rbn_key.setGeometry(QtCore.QRect(20, 50, 321, 17))
        self.rbn_key.setObjectName("rbn_key")
        self.rbn_keypass = QtWidgets.QRadioButton(self.groupBox)
        self.rbn_keypass.setGeometry(QtCore.QRect(20, 80, 311, 17))
        self.rbn_keypass.setObjectName("rbn_keypass")
        self.img_main = QtWidgets.QLabel(self.groupBox)
        self.img_main.setGeometry(QtCore.QRect(250, 20, 81, 81))
        self.img_main.setText("")
        self.img_main.setPixmap(QtGui.QPixmap("images/icon_uug.png"))
        self.img_main.setScaledContents(True)
        self.img_main.setObjectName("img_main")
        self.gbx_key = QtWidgets.QGroupBox(GeokodowanieAdresowDialogBase)
        self.gbx_key.setEnabled(False)
        self.gbx_key.setGeometry(QtCore.QRect(20, 350, 351, 71))
        self.gbx_key.setObjectName("gbx_key")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.gbx_key)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(-1, 10, 351, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_key = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_key.setFont(font)
        self.lbl_key.setObjectName("lbl_key")
        self.horizontalLayout_6.addWidget(self.lbl_key)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.btn_key = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.btn_key.setObjectName("btn_key")
        self.horizontalLayout_6.addWidget(self.btn_key)
        self.label_2 = QtWidgets.QLabel(GeokodowanieAdresowDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 450, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(GeokodowanieAdresowDialogBase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 430, 160, 56))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_test = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_test.setEnabled(True)
        self.btn_test.setObjectName("btn_test")
        self.verticalLayout_3.addWidget(self.btn_test)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_8.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_8.addWidget(self.btn_cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.lbl_summary = QtWidgets.QLabel(GeokodowanieAdresowDialogBase)
        self.lbl_summary.setGeometry(QtCore.QRect(20, 10, 351, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_summary.setPalette(palette)
        self.lbl_summary.setTextFormat(QtCore.Qt.RichText)
        self.lbl_summary.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_summary.setObjectName("lbl_summary")
        self.lbl_server.setBuddy(self.led_server)
        self.lbl_sshport.setBuddy(self.sbx_sshport)
        self.lbl_user.setBuddy(self.led_user)
        self.lbl_pass.setBuddy(self.led_pass)
        self.lbl_rport.setBuddy(self.sbx_rport)
        self.lbl_lport.setBuddy(self.sbx_lport)
        self.lbl_key.setBuddy(self.btn_key)

        self.retranslateUi(GeokodowanieAdresowDialogBase)
        QtCore.QMetaObject.connectSlotsByName(GeokodowanieAdresowDialogBase)
        GeokodowanieAdresowDialogBase.setTabOrder(self.rbn_pass, self.rbn_key)
        GeokodowanieAdresowDialogBase.setTabOrder(self.rbn_key, self.rbn_keypass)
        GeokodowanieAdresowDialogBase.setTabOrder(self.rbn_keypass, self.led_server)
        GeokodowanieAdresowDialogBase.setTabOrder(self.led_server, self.sbx_sshport)
        GeokodowanieAdresowDialogBase.setTabOrder(self.sbx_sshport, self.led_user)
        GeokodowanieAdresowDialogBase.setTabOrder(self.led_user, self.led_pass)
        GeokodowanieAdresowDialogBase.setTabOrder(self.led_pass, self.sbx_rport)
        GeokodowanieAdresowDialogBase.setTabOrder(self.sbx_rport, self.sbx_lport)
        GeokodowanieAdresowDialogBase.setTabOrder(self.sbx_lport, self.btn_key)
        GeokodowanieAdresowDialogBase.setTabOrder(self.btn_key, self.btn_test)
        GeokodowanieAdresowDialogBase.setTabOrder(self.btn_test, self.btn_ok)
        GeokodowanieAdresowDialogBase.setTabOrder(self.btn_ok, self.btn_cancel)

    def retranslateUi(self, GeokodowanieAdresowDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GeokodowanieAdresowDialogBase.setWindowTitle(_translate("GeokodowanieAdresowDialogBase", "Geokodowanie Adresów"))
        self.lbl_server.setToolTip(_translate("GeokodowanieAdresowDialogBase", "address of remote host"))
        self.lbl_server.setText(_translate("GeokodowanieAdresowDialogBase", "SSH server*"))
        self.led_server.setPlaceholderText(_translate("GeokodowanieAdresowDialogBase", "e.g. myserver.mydomain.com"))
        self.lbl_sshport.setText(_translate("GeokodowanieAdresowDialogBase", "SSH port*"))
        self.lbl_user.setText(_translate("GeokodowanieAdresowDialogBase", "SSH User*"))
        self.led_user.setPlaceholderText(_translate("GeokodowanieAdresowDialogBase", "e.g. user123"))
        self.lbl_pass.setText(_translate("GeokodowanieAdresowDialogBase", "SSH Password"))
        self.lbl_rport.setText(_translate("GeokodowanieAdresowDialogBase", "Remote bind port*"))
        self.lbl_lport.setText(_translate("GeokodowanieAdresowDialogBase", "Local bind port*"))
        self.lbl_pluginVersion.setText(_translate("GeokodowanieAdresowDialogBase", "Plugin Name 1.0.0"))
        self.lbl_copyrights.setText(_translate("GeokodowanieAdresowDialogBase", "© 2020 <a href=\"http://www.envirosolutions.pl/\">EnviroSolutions Sp. z o.o.</a>"))
        self.groupBox.setTitle(_translate("GeokodowanieAdresowDialogBase", "Authentication method"))
        self.rbn_pass.setText(_translate("GeokodowanieAdresowDialogBase", "Password"))
        self.rbn_key.setText(_translate("GeokodowanieAdresowDialogBase", "Private Key"))
        self.rbn_keypass.setText(_translate("GeokodowanieAdresowDialogBase", "Key + Password"))
        self.gbx_key.setTitle(_translate("GeokodowanieAdresowDialogBase", "Authentication key"))
        self.lbl_key.setText(_translate("GeokodowanieAdresowDialogBase", "Choose private key file:"))
        self.btn_key.setText(_translate("GeokodowanieAdresowDialogBase", "..."))
        self.label_2.setText(_translate("GeokodowanieAdresowDialogBase", "*required fields"))
        self.btn_test.setText(_translate("GeokodowanieAdresowDialogBase", "Connection test"))
        self.btn_ok.setText(_translate("GeokodowanieAdresowDialogBase", "OK"))
        self.btn_cancel.setText(_translate("GeokodowanieAdresowDialogBase", "Cancel"))
        self.lbl_summary.setText(_translate("GeokodowanieAdresowDialogBase", "<html><head/><body><p><span style=\" color:#aa0000;\">Your remote data will be available on 127.0.0.1:55667</span></p></body></html>"))

