# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 300)
        self.textBrowser = QTextBrowser(Frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QRect(10, 10, 381, 281))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Frame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u042d\u0442\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0430 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043a\u0443\u0440\u0441\u043e\u0432\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u043f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435 \u041e\u0441\u043d\u043e\u0432\u044b "
                        "\u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u043c \u0433\u0440\u0443\u043f\u043f\u044b \u041e\u041f341 \u0413\u043e\u043b\u0435\u0432\u044b\u043c \u041a\u0438\u0440\u0438\u043b\u043b\u043e\u043c \u041e\u043b\u0435\u0433\u043e\u0432\u0438\u0447\u0435\u043c. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0432\u044b\u0447\u0438\u0441\u043b\u044f\u0435\u0442 \u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0435\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u043f\u0440\u0435\u0434"
                        "\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0438\u043d\u0442\u0435\u0433\u0440\u0430\u043b\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0432\u0432\u043e\u0434\u0438\u0442. \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0434\u0438\u043d \u0438\u0437 \u0442\u0440\u0435\u0445 \u0441\u043f\u043e\u0441\u043e\u0431\u043e\u0432: \u043c\u0435\u0442\u043e\u0434 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u0432, \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0439 \u0438 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-style:italic;\">\u0411\u0413\u0410\u0421 2024</span></p></body></html>", None))
    # retranslateUi

