# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connectionqCHhda.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Connection(object):
    def setupUi(self, Connection):
        if not Connection.objectName():
            Connection.setObjectName(u"Connection")
        Connection.resize(161, 107)
        self.verticalLayout = QVBoxLayout(Connection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.ip_label = QLabel(Connection)
        self.ip_label.setObjectName(u"ip_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ip_label)

        self.ip_input = QLineEdit(Connection)
        self.ip_input.setObjectName(u"ip_input")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.ip_input)

        self.port_label = QLabel(Connection)
        self.port_label.setObjectName(u"port_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.port_label)

        self.port_input = QLineEdit(Connection)
        self.port_input.setObjectName(u"port_input")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.port_input)


        self.verticalLayout.addLayout(self.formLayout)

        self.connect_button = QPushButton(Connection)
        self.connect_button.setObjectName(u"connect_button")

        self.verticalLayout.addWidget(self.connect_button)


        self.retranslateUi(Connection)

        QMetaObject.connectSlotsByName(Connection)
    # setupUi

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(QCoreApplication.translate("Connection", u"Form", None))
        self.ip_label.setText(QCoreApplication.translate("Connection", u"IP:", None))
        self.port_label.setText(QCoreApplication.translate("Connection", u"Port:", None))
        self.connect_button.setText(QCoreApplication.translate("Connection", u"Connect", None))
    # retranslateUi

