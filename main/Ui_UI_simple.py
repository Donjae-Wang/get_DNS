# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_simple.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 495)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.open_hosts_path_b = QPushButton(self.centralwidget)
        self.open_hosts_path_b.setObjectName(u"open_hosts_path_b")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.open_hosts_path_b.setFont(font)

        self.gridLayout.addWidget(self.open_hosts_path_b, 3, 2, 1, 1)

        self.flush_dns_b = QPushButton(self.centralwidget)
        self.flush_dns_b.setObjectName(u"flush_dns_b")
        self.flush_dns_b.setFont(font)

        self.gridLayout.addWidget(self.flush_dns_b, 3, 3, 1, 1)

        self.get_b = QPushButton(self.centralwidget)
        self.get_b.setObjectName(u"get_b")
        self.get_b.setFont(font)

        self.gridLayout.addWidget(self.get_b, 3, 0, 1, 1)

        self.output_text = QTextBrowser(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setFont(font)

        self.gridLayout.addWidget(self.output_text, 1, 0, 1, 4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.copy_b = QPushButton(self.centralwidget)
        self.copy_b.setObjectName(u"copy_b")
        self.copy_b.setFont(font)

        self.gridLayout.addWidget(self.copy_b, 3, 1, 1, 1)

        self.pg_bar = QProgressBar(self.centralwidget)
        self.pg_bar.setObjectName(u"pg_bar")
        self.pg_bar.setFont(font)
        self.pg_bar.setValue(0)

        self.gridLayout.addWidget(self.pg_bar, 2, 0, 1, 4)

        self.domain_text = QLineEdit(self.centralwidget)
        self.domain_text.setObjectName(u"domain_text")
        self.domain_text.setFont(font)

        self.gridLayout.addWidget(self.domain_text, 0, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 806, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.copy_b.clicked.connect(self.output_text.copy)
        self.copy_b.clicked.connect(self.output_text.selectAll)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Get GitHub DNS", None))
        self.open_hosts_path_b.setText(QCoreApplication.translate("MainWindow", u"Open Hosts Folder", None))
#if QT_CONFIG(whatsthis)
        self.flush_dns_b.setWhatsThis(QCoreApplication.translate("MainWindow", u"windows needs to click this button", None))
#endif // QT_CONFIG(whatsthis)
        self.flush_dns_b.setText(QCoreApplication.translate("MainWindow", u"DNS Flush", None))
        self.get_b.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Domain Name(default github):", None))
        self.copy_b.setText(QCoreApplication.translate("MainWindow", u"Copy(Double Click)", None))
#if QT_CONFIG(tooltip)
        self.domain_text.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>If more than one , sep with Space(&quot; &quot;).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

