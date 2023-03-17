# example PyQt panel that implements a simple web browser in Nuke

import sip
import nuke
import nukescripts
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *


class WebBrowserWidget(QWidget):
    def changeLocation(self):
        self.webView.load(QUrl(self.locationEdit.text()))

    def __init__(self):
        super(QWidget, self).__init__()
        self.webView = QWebView()

        self.setLayout(QVBoxLayout())

        self.locationEdit = QLineEdit('http://www.google.com')
        self.locationEdit.setSizePolicy(
            QSizePolicy.Expanding, self.locationEdit.sizePolicy().verticalPolicy())

        QObject.connect(self.locationEdit, SIGNAL(
            'returnPressed()'),  self.changeLocation)

        self.layout().addWidget(self.locationEdit)

        bar = QToolBar()
        bar.addAction(self.webView.pageAction(QWebPage.Back))
        bar.addAction(self.webView.pageAction(QWebPage.Forward))
        bar.addAction(self.webView.pageAction(QWebPage.Stop))
        bar.addAction(self.webView.pageAction(QWebPage.Reload))
        bar.addSeparator()

        self.layout().addWidget(bar)
        self.layout().addWidget(self.webView)

        self.webView.load(QUrl('http://www.google.com'))


class WebBrowserKnob():

    def makeUI(self):
        self.webWidget = WebBrowserWidget()
        return self.webWidget


class WebBrowserPanel(nukescripts.PythonPanel):

    def __init__(self):
        super(WebBrowserPanel, self).__init__(
            'Web Browser', 'uk.co.thefoundry.WebBrowserPanel')
        self.webBrowserKnob = nuke.PyCustom_Knob(
            'web', '', 'nukescripts.pyQtExamples.webBrowser.WebBrowserKnob()')
        self.addKnob(self.webBrowserKnob)


def addPanel():
    return WebBrowserPanel().addToPane()


menu = nuke.menu('Pane')
menu.addCommand('Web Browser', addPanel)
nukescripts.registerPanel('uk.co.thefoundry.WebBrowserPanel', addPanel)
