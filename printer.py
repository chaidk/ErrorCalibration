
'''

import win32print
import win32ui
from PIL import Image, ImageWin

#
# Constants for GetDeviceCaps
#
#
# HORZRES / VERTRES = printable area
#
HORZRES = 8
VERTRES = 10
#
# LOGPIXELS = dots per inch
#
LOGPIXELSX = 88
LOGPIXELSY = 90
#
# PHYSICALWIDTH/HEIGHT = total area
#
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111
#
# PHYSICALOFFSETX/Y = left / top margin
#
PHYSICALOFFSETX = 112
PHYSICALOFFSETY = 113

printer_name = win32print.GetDefaultPrinter ()
file_name = r"C:/Users/ChaiPC/Documents/github/ErrorCalibration-main/test.png"

#
# You can only write a Device-independent bitmap
#  directly to a Windows device context; therefore
#  we need (for ease) to use the Python Imaging
#  Library to manipulate the image.
#
# Create a device context from a named printer
#  and assess the printable size of the paper.
#
hDC = win32ui.CreateDC ()
hDC.CreatePrinterDC (printer_name)
printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)

#
# Open the image, rotate it if it's wider than
#  it is high, and work out how much to multiply
#  each pixel by to get it as big as possible on
#  the page without distorting.
#
bmp = Image.open (file_name)
if bmp.size[0] > bmp.size[1]:
  bmp = bmp.rotate (90)

ratios = [0.5 * printable_area[0] / bmp.size[0], 0.5 * printable_area[1] / bmp.size[1]]
scale = min (ratios)

#
# Start the print job, and draw the bitmap to
#  the printer device at the scaled size.
#
hDC.StartDoc (file_name)
hDC.StartPage ()

dib = ImageWin.Dib (bmp)
scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
x1 = int ((printer_size[0] - scaled_width) / 2)
y1 = int ((printer_size[1] - scaled_height) / 2)
x2 = x1 + scaled_width
y2 = y1 + scaled_height
dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))

hDC.EndPage ()
hDC.EndDoc ()
hDC.DeleteDC ()

'''


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog
from PyQt5.QtCore import QUrl, QSizeF, QMarginsF
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebEngineWidgets import *
from Ui_report import Ui_reportwin, QtCore
from sys import argv, exit
import os
import selenium
import win32print

def print_completed(self):
    print(1)


class ReportForm(QDialog, Ui_reportwin):
    def __init__(self):
        super(ReportForm, self).__init__()
        self.setupUi(self)
        self.browser.load(QUrl('file:///test.html'))

    def screen_shot(self):
        try:
            os.system('cd app && temdata002.html')
            print(1)
            # win32print.SetDefaultPrinter("Microsoft Print to PDF")
            # printer = QPrinter()
            # printer.setPageSizeMM(QSizeF(80, 300))
            # # self.browser.page().runJavaScript('alert(window.print())')
            # self.browser.page().print(printer, print_completed)
        except Exception as e:
            print(repr(e))


if __name__ == '__main__':

    app = QApplication(argv)
    reportWindow = ReportForm()
    reportWindow.show()
    exit(app.exec_())
